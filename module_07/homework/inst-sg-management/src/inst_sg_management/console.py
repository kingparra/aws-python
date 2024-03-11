#!/usr/bin/env python3
import boto3
import jinja2
import uuid
import textwrap

from inst_sg_management.functions import *


def main():
    ec2 = boto3.resource('ec2')

    # Create five instances with a SG that allows SSH ingress
    vpc = first(vpcs_named(ec2, 'PYTHON-VPC'))
    sg = sg_with_ssh_ingress(ec2, vpc.id, f'boto3-sg-{uuid.uuid4()}', 'Allow SSH ingress')
    ami = latest_amzl_ami(ec2)
    subnet_id = first(subnets_named(
        ec2, vpc_id=vpc.id,
        subnet_name='PYTHON-VPC-public-subnet-1')).id
    instances = create_instances(
        ec2,
        count=5,
        subnet_id=subnet_id,
        sg_id=sg.id,
        key_name="python-class-kp",
        ami=ami,
        itype="t2.micro",
        iname="YellowTail")

    # Print a report of running_instances, security_groups, unused_security_groups
    report = textwrap.dedent(
        """
        Created Instances
        -----------------
        {% for instance in instances %}
        {{instance.id}}
        {% endfor %}

        Running Instances
        -----------------
        {% for instance in running_instances %}
        {{instance.id}}
        {% endfor %}

        Security Groups
        ---------------
        {% for sg in sgs %}
        {{sg.id}}
        {% endfor %}

        Unused Security Groups
        ----------------------
        {% for un in unused_sgs %}
        {{un.id}}
        {% endfor %}

        """)

    environment = jinja2.Environment()
    template = environment.from_string(report)

    running_instances, all_sgs, unused_sgs = generate_report(ec2)

    print(template.render(
            instances=instances,
            running_instances=running_instances,
            sgs=all_sgs,
            unused_sgs=unused_sgs))
