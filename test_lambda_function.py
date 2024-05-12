import pytest
from lambda_function import lambda_handler

def test_lambda_handler():
    event = {}
    context = {}
    response = lambda_handler(event, context)
    assert 'currentTime' in response['body']
