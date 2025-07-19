from django.test import TestCase
from django.http import HttpResponse

from pytest_django.fixtures import client

def test_home_return_in_httpresponse_status_code_200(client):
    request = client.get("/")
    assert request.status_code == 200

