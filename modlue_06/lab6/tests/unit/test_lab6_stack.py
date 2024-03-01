import aws_cdk as core
import aws_cdk.assertions as assertions

from lab6.lab6_stack import Lab6Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in lab6/lab6_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Lab6Stack(app, "lab6")
    template = assertions.Template.from_stack(stack)
