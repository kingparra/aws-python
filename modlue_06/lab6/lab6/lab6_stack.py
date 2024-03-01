from aws_cdk import (
    aws_autoscaling as autoscaling,
    aws_ec2 as ec2,
    aws_s3 as s3,
    aws_elasticloadbalancingv2 as elbv2,
    App,
    CfnOutput,
    Stack
    )
from constructs import Construct
import textwrap




class Lab6Stack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        vpc = ec2.Vpc(self, "VPC")
