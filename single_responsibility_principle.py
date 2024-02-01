# (srp) single responsibiliy principle is the principle created in 1989 by Robert C. martin surnamed
# uncle BOB, a well-known figure in software developpement and he was officially a signatory of AGILE SOFTWARE
# he stated that rsp means that a class should have one responsibility and one reason to change, for a better
# clarification this principle is similar to the concept of separate concerns,  which means a programing concept  should split
# into different sections and each section should manage diverse concerns

# a class being created  that has only the responsibility to manage a Student information
from typing import Self
import math
import pprint

class Student:
    def __init__(self: Self, Id_representation: str, Firstname: str, Lastname: str, Password: int, Email: str, average: int | None) -> Self:
        self.Id_reprensentation = Id_representation
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.Password = Password
        self.Email = Email
        self.average = average
        
        @property
        def Get_Firstname(self: Self) -> str:
            return self.Firstname
        
        @Get_Firstname.setter
        def set_firstname(self: Self, firstname: str):
            self.Firstname = firstname
            return self.Firstname

        @property
        def Get_Lastname(self: Self) -> str:
            return self.Lastname
        
        @Get_Lastname.setter
        def set_Lastname(self: Self, lastname: str) -> str:
            self.Lastname = lastname
            return self.Lastname
        
        @property
        def Get_Password(self: Self) -> int:
            return self.Password
        
        @Get_Password.setter
        def set_password(self: Self, new_password: int) -> int:
            self.Password = new_password
            return self.Password
            
        @property
        def Get_Email(self: Self) -> str:
            return self.Email
        
        @Get_Email.setter
        def set_email(self: Self, new_email: str) -> str:
            self.Email = new_email
            return self.Email
        
        @property
        def Get_average(self: Self) -> int:
            return self.average
        
        @Get_average.setter
        def set_average(student_average: int) -> average:
            self.average = student_average
            return self.average

# this class has only one responsibility that is to calculate the student average
class CalculateAverage:
    # a Private Total Point attribute with a number on which to calculate student average
    __Point: int = 100
    
    def __init__(self: Self, Id_representation: str) -> Self:
        self.Id_representation = Id_representation

    def average(self: Self, note: int) -> int:
        if not self.Id_representation:
            raise NotImplementedError("Sorry the student must be identified")
        if note is None:
            raise NotImplementedError("Sorry, student note must be entered")
        student_average = math.floor((self.__Point * note) / 100)
        return student_average


# create a student instanciation
student: Student = Student(Id_representation="1234dkdjd44", Firstname="romeus", Lastname="clarens",
                       Password=12345 , Email="clarensromeus10@gmail.com", average=None)

# display all the user informations
pprint.pprint(dict(student.__dict__.items()), sort_dicts=False)
# change some of the user informations
student.Firstname = "allrich"
student.Email = "allrichromeusclarens"
student.Password = 8884412
# now call the CalculateAverage class to calculate the user average
calculate_average = CalculateAverage(Id_representation="1234dkdjd44")
student.average = calculate_average.average(note=78)
# now after modifying some of the Student class fields 
pprint.pprint(dict(student.__dict__.items()), sort_dicts=False)


