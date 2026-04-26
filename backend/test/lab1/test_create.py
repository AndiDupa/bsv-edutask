import pytest
from unittest.mock import MagicMock

# from src.controllers.usercontroller import UserController
from src.util.dao import DAO
import pymongo
from dotenv import dotenv_values

# create a data access object
from src.util.validators import getValidator

import json
from bson import json_util
from bson.objectid import ObjectId

@pytest.fixture
def dao():
    dao = DAO("user")
    dao.collection.delete_many({})

    return dao

def test_create_compliant_data(dao):
    result = dao.create({"firstName": "Andi", "lastName": "Dupa", "email": "andi@gmail.com"})

    assert result["firstName"] == "Andi"
    assert result["lastName"] == "Dupa"
    assert result["email"] == "andi@gmail.com"

def test_create_not_compliant_data(dao):
    with pytest.raises(Exception) as _:
        dao.create({"city": "Karlskrona", "country": "Sweden", "continent": "Europe"})

def test_create_unique(dao):
    dao.create({"firstName": "Andi", "lastName": "Dupa", "email": "andi@gmail.com"})
    result = dao.create({"firstName": "Andi", "lastName": "Dupa", "email": "andi@gmail.com"})

    assert result["firstName"] == "Andi"
    assert result["lastName"] == "Dupa"
    assert result["email"] == "andi@gmail.com"
