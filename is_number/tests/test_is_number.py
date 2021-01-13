from datetime import datetime

from is_number import is_number


def test_is_number():
    assert is_number(1)


def test_is_not_number():
    assert not is_number("Hello world")
    assert not is_number({"Hello": "world"})
    assert not is_number(datetime.now())
    assert not is_number(lambda foo: foo)
