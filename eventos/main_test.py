import flask
import pytest

import main

@pytest.fixture(scope="module")
def app():
  return flask.Flask(__name__)

def test_hello_get(app):
  with app.test_request_context():
    res = main.hello_get(flask.request)
    assert 'Hello World!' in res

def test_hello_http_no_args(app):
  with app.test_request_context():
    res = main.hello_http(flask.request)
    assert 'Hello World!' in res

def test_hello_http_get(app):
  with app.test_request_context(query_string={'name': 'test'}):
    res = main.hello_http(flask.request)
    assert 'Hello test!' in res

def test_hello_http_args(app):
  with app.test_request_context(json={'name': 'test'}):
    res = main.hello_http(flask.request)
    assert 'Hello test!' in res

def test_hello_http_empty_json(app):
  with app.test_request_context(json=''):
    res = main.hello_http(flask.request)
    assert 'Hello World!' in res

def test_hello_http_xss(app):
  with app.test_request_context(json={'name': '<script>alert(1)</script>'}):
    res = main.hello_http(flask.request)
    assert '<script>' not in res

