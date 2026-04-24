from service import UserService
import pytest


def test_create_and_get_user():
    service = UserService()
    service.create_user("Ashu", 25)
    user = service.get_user("Ashu")
    assert user.name == "Ashu"


def test_user_not_found():
    service = UserService()
    with pytest.raises(Exception):
        service.get_user("Unknown")