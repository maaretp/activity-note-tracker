from approvaltests.approvals import verify

from hello_world import hello_world


def test_pytest_works():
    assert True
    verify("foo")


def test_hello_world():
    assert(hello_world(), 'Hello World!')
