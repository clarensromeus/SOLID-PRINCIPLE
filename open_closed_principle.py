#(OCP) Open-closed principle, it is coined by Bertrand meyer in 1988, he stated that software entities 
# like (Classes, interfaces, modules) should always open for extension and closed for modification,
# this way the code becomes more clean, separate, easier to extend and and unaltered


from abc import ABC, abstractmethod
from typing import Self
import pprint
from enum import Enum, verify, UNIQUE

# create an enum of unique previlege for any class
@verify(UNIQUE)
class Privilege(str, Enum):
    MINOR = "MINOR"
    MAJOR = "MAJOR"
    FULL = "FULL"

# create an abstract Employee class 
class Employee(ABC):
    def __init__(self, privilege: str) -> Self:
        super().__init__()
        self.privilege = privilege
        
    @abstractmethod
    def rating(self: Self, hours_per_weeks: int, perks: int):
        raise NotImplementedError("Sorry, impossible implementation")

# create an abstract Administration class
class Administrator(ABC):
    def __init__(self, privilege: str, experience_time: int) -> Self:
        super().__init__()
        self.privilege = privilege
        self.experience_time = experience_time
        
    @abstractmethod
    def rating(self: Self, time_of_working: int, perks: int):
        raise NotImplementedError("Sorry, impossible implementation")
    
# make the concrete Manager class inherits the abstract Employee class
class Manager(Employee):
    def __init__(self, privilege: str, salary: float) -> Self:
        super().__init__(privilege)
        self.salary = salary 
        
    def rating(self: Self, hours_per_weeks: str, perks: int) -> int:
        self.salary = round(hours_per_weeks * perks / 2)
        return self.salary
    
# make the concrete Engineer class inherits the abastract Adminsitrator class     
class Engineer(Administrator):
    def __init__(self, privilege: int, salary: int, experience_time: int) -> Self:
        super().__init__(privilege, experience_time)
        self.salary = salary
        
    def rating(self: Self, hours_per_weeks: int, perks: int) -> int:
        self.salary =  round(hours_per_weeks * perks / 2)
        return self.salary

# make the concrete CEO class inherits the abstract Administrator class    
class CEO(Administrator):
    def __init__(self, privilege: int, salary: float, experience_time: int) -> Self:
        super().__init__(privilege, experience_time)
        self.salary = salary
        
    def rating(self: Self, hours_per_weeks: int, perks: int) -> int: 
        self.salary = round(hours_per_weeks * perks / 2) 
        return self.salary
        

# start intanciating the manager class with an initial salary of an ammount of 0.00
manager: Manager = Manager(privilege=Privilege.MINOR, salary=0)
# calculate the manager rating
pprint.pprint(dict(manager.__dict__.items()))
# calculate and display the manager salary
manager_average = manager.rating(hours_per_weeks=8, perks=20)
pprint.pprint(manager_average, sort_dicts=False)
# start instanciating the Engineer class with an initial ammount of 0.00
engineer: Engineer = Engineer(privilege=Privilege.MAJOR, salary=0, experience_time=13)
pprint.pprint(dict(engineer.__dict__.items()), sort_dicts=False)
# calculate and display the Engineer salary
engineer_average = engineer.rating(hours_per_weeks=20, perks=80)
pprint.pprint(engineer_average, sort_dicts=False)
# start instanciating the CEO class with an initial ammount of 0.00
ceo: CEO = CEO(privilege=Privilege.FULL, salary=0.00, experience_time=24)
pprint.pprint(dict(ceo.__dict__.items()), sort_dicts=False)
# calculate and display the CEO salary 
pprint.pprint(ceo.rating(hours_per_weeks=20, perks=100), sort_dicts=False)



        
        
        
    
        
        
        