# (LSP) liskov substitution principle is the third principle conceived by Barbara liskov at an OOPSLAR 
# conference in 1988, where this principle is revealed in her programming design book, what this principle
# means is that subtypes should be substitutable with their base types, henceforth subclasses have to represent their base classes
# let' s say that we have base object T with a child S and S should redefine or implement all methods in the object T


from abc import ABC, abstractmethod
import pprint
from enum import Enum, verify, UNIQUE
from typing import Self, Any
import random
import math

# a unique enum defining members hours 
@verify(UNIQUE)
class Hours(int, Enum):
    FEW = 7
    AVERAGE = 12
    EXCELLENT = 20

# a unique enum defining members days
@verify(UNIQUE)
class Days(int, Enum):
    FEW = 2
    AVERAGE = 4
    EXCELLENT = 6

class Member(ABC):
    def __init__(self, school_name: str, session: str) -> Self:
        super().__init__()
        self.school_name = school_name
        self.session = session
        
        @abstractmethod
        def member_presence(self: Self, hours_per_week: Any, task: str):
            raise NotImplementedError("Sorry, impossible implementation")
        
        @abstractmethod
        def member_schedule(self: Self, hours: int, days: int):
            raise NotImplementedError("Sorry, impossible implementation")

# creation of the SchoolBoard with with 2 methods
class SchoolBoard(Member):
    __schedule: dict[str, int | str]
    __total_presence: int
    
    def __init__(self, school_name: str, session: str, member_id: int, member_name: str) -> Self:
        super().__init__(school_name, session)
        self.member_id = member_id
        self.member_name = member_name
        
    def member_presence(self: Self, hours_per_week: list[int], task: int) -> int:
        presence_calculation = math.floor(sum(hours_per_week) / task)
        self.__total_presence = presence_calculation
        return self.__total_presence
    
    def member_schedule(self: Self, hours: int, days: int) -> dict[str, int | int]:
        self.__schedule = {"hours": hours, "days": days}
        return self.__schedule

# Teacher class creation with 2 overriden methods that were created in the Schoolboard class 
class Teacher(Member):
    __schedule: dict[str, int | str]
    __total_presence: int
    
    def __init__(self, school_name: str, session: str, teacher_id: int, teacher_name: str) -> Self:
        super().__init__(school_name, session)
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        
    def member_presence(self: Self, hours_per_week: int, task: int) -> int:
        presence_calculation = math.floor(hours_per_week / task)
        self.__total_presence = presence_calculation
        return self.__total_presence
    
    def member_schedule(self: Self, hours: int, days: int) -> dict[str, str | int]:
        self.__schedule = {"hours": hours, "days": days}
        return self.__schedule
        
# Student class creation with 2 overriden methods that were created in the SchoolBoard class
class Student(Member):
    __schedule: dict[str, int | str]
    __total_presence: int
    
    def __init__(self, school_name: str, session: str, student_id: int, student_name: str) -> Self:
        super().__init__(school_name, session)
        self.student_id = student_id
        self.student_name = student_name
        
    def member_presence(self: Self, hours_per_week: int, task: int) -> int:
        presence_calculation = math.floor(hours_per_week / task)
        self.__total_presence = presence_calculation
        return self.__total_presence
    
    def member_schedule(self: Self, hours: int, days: int) -> dict[str, int | str]:
        self.__schedule = {"hours": hours, "days": days}
        return self.__schedule
    

# start by instanciating the School class
school: SchoolBoard = SchoolBoard(school_name="IDOL", session="2nd", member_id=random.randint(1, 9), member_name="clarensromeus")
# display the all the School class input
pprint.pprint(dict(school.__dict__.items()), sort_dicts=False)
# display all the School class inner methods 
pprint.pprint(school.member_presence(hours_per_week=[3, 5, 6, 7, 20], task=6))
pprint.pprint(school.member_schedule(hours=Hours.EXCELLENT.value, days=Days.EXCELLENT.value))
# instanciation proccess of the Teacher class
teacher: Teacher = Teacher(school_name="OLIMPIA MOHA", session="1st", teacher_id=random.randint(1, 9), teacher_name="Robert Kiyosaki")
# display all the Teacher inputs
pprint.pprint(dict(teacher.__dict__.items()), sort_dicts=False)
# display all the Teacher class inner methods 
pprint.pprint(teacher.member_presence(hours_per_week=20, task=4))
pprint.pprint(teacher.member_schedule(hours=Hours.AVERAGE, days=Days.AVERAGE))
# instanciation process of the Student class
student: Student = Student(school_name="MALETTI PIER", session="3rd", student_id=random.randint(1, 9), student_name="prophete allrich")
# display all the Student inputs
pprint.pprint(dict(student.__dict__.items()))
# display all the Students class inner methods
pprint.pprint(student.member_presence(hours_per_week=24, task=2))
pprint.pprint(student.member_schedule(hours=Hours.FEW, days=Days.FEW))