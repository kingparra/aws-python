#!/usr/bin/env python3
import os

import aws_cdk as cdk

from lab6.lab6_stack import Lab6Stack


app = cdk.App()
Lab6Stack(app, "Lab6Stack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region='us-east-1'),
    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

app.synth()
