# (DIP) Dependency inversion principle, it means that abstraction should not depend upon detail, but 
# details should upon abtractions

import random
from typing import Self
from enum import Enum, UNIQUE, verify
import pprint
from abc import abstractmethod, ABCMeta

@verify(UNIQUE)
class Case(str, Enum):
    USER = "USER"
    COMPANY = "COMPANY"

database: dict[str, dict[str, int | str | bool]]  = {
    "clarensromeus": {
        "id": random.randint(1, 100),
        "username": "clarensromeus",
        "email": "clarensromeus10@gmail.com",
        "active": True
    },
    "clervilwoodlet": {
        "id": random.randint(1, 100),
        "username": "clervilwoodlet",
        "email": "clervilwoodlet33@gmail.com",
        "active": False
    },
    "propheteallrich": {
        "id": random.randint(1, 100),
        "username": "propheteallrich",
        "email": "propheteallrich45@gmail.com",
        "active": True
    }
}

api_data: dict[str, dict[str, str | int]] = {
    "united states power": {
        "company": "United states power",
        "customer": 700,
        "branches": 5
    },
    "Techy trans": {
        "company": "Techy trans",
        "customer": 1009,
        "branches": 60
    },
    "rockefeller oil": {
        "company": "Rockefeller oil",
        "customer": 500,
        "branches": 40
    }
}


class RiverSchool:
    __single_user: dict[str, dict[str, str | int | bool]]
    
    def __init__(self: Self, datasource, identity_case: str) -> Self:
        self.datasource = datasource
        self.identity_case = identity_case
        
    def display_data(self: Self) -> dict[str, dict[str, str | int | bool]]:
        return self.datasource.get_data()
    
    def display_single_data(self: Self, name: str)-> dict[str, dict[str | int | bool]]:
        self.__single_user = self.datasource.get_data()[name]
        return self.__single_user
    
# creation of an abstract class upon which data delivery decision should make    
class DataSource(metaclass=ABCMeta):
    @abstractmethod
    def get_data(self: Self):
        raise NotImplementedError("Sorry, impossible implementation")

# concrete class which depends upon abstraction to share database data
class Database(DataSource):
    def get_data(self: Self) -> dict[str, dict[str, str | int | bool]]:
        return database
    
# concrete class which depends upon abstraction to share thirdpartyapi data
class ThirdPartyApi(DataSource):
    def get_data(self: Self) -> dict[str, dict[str, str | int]]:
        return api_data


# instantiating Riverschool class which  will display data from the application database 
riverschoolDatabase: RiverSchool = RiverSchool(datasource=Database(), identity_case=Case.USER.value)
# <------------------- display all the RiverSchool' users data ------------------> #
pprint.pprint(riverschoolDatabase.display_data(), sort_dicts=False)
# <------------------- display only single user data from the RiverSchool -----------------> #
pprint.pprint(riverschoolDatabase.display_single_data(name="clervilwoodlet"), sort_dicts=False)
# instantiating RiverSchool class wich will display data from the ThirdParty application
riverschoolThirdpartyapi: RiverSchool = RiverSchool(datasource=ThirdPartyApi(), identity_case=Case.COMPANY.value)
# <------------------- display all the RiverSchool' companies data ------------------> #
pprint.pprint(riverschoolThirdpartyapi.display_data(), sort_dicts=False)
# <------------------- display only single company data from the RiverSchool -----------------> #
pprint.pprint(riverschoolThirdpartyapi.display_single_data(name="Techy trans"), sort_dicts=False)
    
