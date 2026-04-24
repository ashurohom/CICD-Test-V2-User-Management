from user import User
import pytest


def test_create_user():
    user = User("Ashu", 25)
    assert user.name == "Ashu"


def test_invalid_age():
    with pytest.raises(ValueError):
        User("Test", -1)