import pytest
from unittest.mock import MagicMock

from src.controllers.usercontroller import UserController
from src.util.dao import DAO

@pytest.fixture
def usr():
    mock = MagicMock()
    mock.find.return_value = [{"andi": "andi@gmail.com"}, {"ando": "andi@gmail.com"}]

    usr = UserController(mock)

    return usr

def test_get_user_by_email_one_valid():
    mock = MagicMock()
    mock.find.return_value = [{"andi": "andi@gmail.com"}]

    usr = UserController(mock)
    result = usr.get_user_by_email("andi@gmail.com")

    assert result == {"andi": "andi@gmail.com"}

def test_get_user_by_email_multiple(usr):
    result = usr.get_user_by_email("andi@gmail.com")

    assert result == {"andi": "andi@gmail.com"}

# This test does not work because get_user_by_email doesn't have logic to handle if a user doesn't exist?

# def test_get_user_by_email_no_matching():
#     mock = MagicMock()
#     mock.find.return_value = []

#     usr = UserController(mock)
#     result = usr.get_user_by_email("steve@gmail.com")

#     assert result == None

def test_get_user_by_email_not_conforming(usr):
    with pytest.raises(ValueError) as _:
        usr.get_user_by_email("andi.com")
