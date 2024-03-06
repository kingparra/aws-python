#!/usr/bin/env python3
# This script implements questions 1 through 3.
import boto3

ec2client = boto3.client('ec2')  # returns json
ec2 = boto3.resource('ec2')  # returns objects

vpc_id = [str(vpc.id) for vpc in ec2.vpcs.all()
          if {'Key': 'Name', 'Value': 'PYTHON-VPC'} in vpc.tags][0]
print(f"vpc_id: {vpc_id}")

public_subnet_1_id = \
    list(ec2.subnets.filter(
        Filters=[
            {"Name": "vpc-id", "Values": [vpc_id]},
            {'Name': 'tag:Name', 'Values': ['PYTHON-VPC-public-subnet-1']}
            ]
        ))[0].id

# Generate a list of amazon linux 2 ami ids
img_response = ec2client.describe_images(
    Filters=[
        {'Name': 'name', 'Values': ['amzn2-ami-hvm-*']},
        {'Name': 'description', 'Values': ['Amazon Linux 2 AMI*']},
        {'Name': 'architecture', 'Values': ['x86_64']},
        {'Name': 'root-device-type', 'Values': ['ebs']},
    ],
    Owners=['amazon']
)

# Get the most recent ami from the list
latest_ami_id = sorted(img_response['Images'],
                       key=lambda x: x['CreationDate'],
                       reverse=True)[0]['ImageId']

# Create a security group that allows ssh ingress
sg = ec2.create_security_group(
  GroupName='boto3-instance-sg',
  Description='SG for instance created with boto3',
  VpcId=vpc_id
)

sg.authorize_ingress(
    IpPermissions=[
        {
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 22,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        }
    ]
)


instances = ec2.create_instances(
    ImageId=latest_ami_id,
    InstanceType='t2.micro',
    KeyName='python-class-kp',
    NetworkInterfaces=[
        {
            'AssociatePublicIpAddress': True,
            'DeviceIndex': 0,
            'Groups':  [sg.group_id],
            'SubnetId': public_subnet_1_id,
        },
    ],
    TagSpecifications=[{
      'ResourceType': 'instance',
      'Tags': [{'Key': 'Name', 'Value': 'boto3-instance'}]}],
    Monitoring={'Enabled': True},
    MinCount=5,
    MaxCount=5
    )


for instance in instances:
  try:
    # Wait until the instance is up
    instance.wait_until_running()
    # Refresh the ip info
    instance.reload()
    print(f"{instance.instance_id} is up and running on {instance.public_ip_address}")
  except Error as e:
    print(f"{instance.instance_id} cannot launch")
