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


data = textwrap.dedent("""
    #!/usr/bin/env bash
    yum install httpd -y
    systemctl enable --now httpd
    cat > /var/www/html/index.html << EOF
    <html>
        <head>
            <title> Example Web Server</title>
        </head>
        <body>
            <div>
                <center>
                    <h2>Welcome AWS $(hostname -f)</h2>
                    <hr/>
                    $(curl "http://169.254.169.254/latest/meta-data/instance-id")
                </center>
            </div>
        </body>
    </html>
    EOF
    """)


class Lab6Stack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        vpc = ec2.Vpc(self, "VPC")
        user_data = ec2.UserData.for_linux().add_commands(data)
