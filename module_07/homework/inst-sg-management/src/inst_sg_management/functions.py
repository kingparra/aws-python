import boto3


ec2 = boto3.resource("ec2")


def first(coll):
    """Return the first element of an iterable"""
    return next(iter(coll))


def vpcs_named(ec2, name):
    """Given a name return a collection of vpc objects"""
    return ec2.vpcs.filter(
        Filters=[{"Name": "tag:Name",
                  "Values": [name]}])


def subnets_named(ec2, vpc_id, subnet_name):
    """Given a subnet name and vpc id, return a collection of subnet objects"""
    return ec2.subnets.filter(
        Filters=[
            {"Name": "vpc-id", "Values": [vpc_id]},
            {"Name": "tag:Name", "Values": [subnet_name]}
            ]
        )


def latest_amzl_ami(ec2):
    """Return the AMI ID of the latest Amazon Linux 2 image"""
    amis = ec2.images.filter(
        Filters=[
            {"Name": "name",             "Values":     ["amzn2-ami-hvm-*"]},
            {"Name": "description",      "Values": ["Amazon Linux 2 AMI*"]},
            {"Name": "architecture",     "Values":              ["x86_64"]},
            {"Name": "root-device-type", "Values":                 ["ebs"]},
        ],
        Owners=["amazon"]
    )
    amis_by_date = sorted(amis, key=(lambda x: x.creation_date), reverse=True)
    latest_ami_id = amis_by_date[0].id
    return latest_ami_id


def sg_with_ssh_ingress(ec2, vpc_id, sg_name, description):
    """Return a security group object with an ingress rule that allows ssh"""
    sg = ec2.create_security_group(
      GroupName=sg_name,
      Description=description,
      VpcId=vpc_id
    )

    def ip_permissions_template(proto, from_port, to_port, cidr):
        return {
            "IpProtocol": proto,
            "FromPort": from_port,
            "ToPort": to_port,
            "IpRanges": [{"CidrIp": cidr}]
        }

    sg.authorize_ingress(
        IpPermissions=[
            ip_permissions_template("tcp", 22, 22, "0.0.0.0/0")
        ]
    )
    return sg


def get_unused_sg_ids():
    """Return security group IDs that are not being used by running instances"""
    running_instances = list(ec2.instances.filter(
        Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
    ))
    all_sgs = set(list(ec2.security_groups.all()))
    used_sgs = set([group.get("GroupId")
                   for instance in running_instances
                   for group in instance.security_groups])
    unused_sgs = all_sgs - used_sgs
    return unused_sgs


def terminate_named(name):
    instances = ec2.instances.filter(
        Filters=[{"Name": "tag:Name", "Values": [name]}]
        )
    for instance in instances:
        instance.terminate()


def generate_report(ec2):
    # list all running ec2 instances
    running_instances = list(ec2.instances.filter(
        Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
    ))
    # list all security groups
    all_sgs = set(list(ec2.security_groups.all()))
    # list sgs that are not being used
    used_sgs = set([group.get("GroupId")
                   for instance in running_instances
                   for group in instance.security_groups])
    unused_sgs = all_sgs - used_sgs
    return (running_instances, all_sgs, unused_sgs)


def get_instance_name(instance):
    for tag in instance.tags or []:
        if tag["Key"] == "Name":
            return tag["Value"]


def create_instances(ec2, count, subnet_id, sg_id, key_name, ami, itype, iname):
    return ec2.create_instances(
        ImageId=ami,
        InstanceType=itype,
        KeyName=key_name,
        NetworkInterfaces=[
            {
                'AssociatePublicIpAddress': True,
                'DeviceIndex': 0,
                'Groups':  [sg_id],
                'SubnetId': subnet_id,
            },
        ],
        TagSpecifications=[{
          'ResourceType': 'instance',
          'Tags': [{'Key': 'Name', 'Value': iname}]}],
        Monitoring={'Enabled': True},
        MinCount=count,
        MaxCount=count
        )
