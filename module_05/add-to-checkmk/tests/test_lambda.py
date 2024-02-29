import add_to_checkmk
import pytest


def test_handler_response():
    assert add_to_checkmk.lambda() == {
        'statusCode': 200,
        'body': json.dumps("Hello from Lambda!")
    }
