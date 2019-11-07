import datetime

from typing import List, Optional


class Classroom:
    warnings: List[str] = []

    def __init__(self, name: str):
        self._name = name
        self._students: List[Student] = []
    
    def get_name(self) -> str:
        return self._name
    
    def set_name(self, value: str) -> None:
        self._name = value
    
    def add_student(self, student: "Student") -> None:
        if student in self._students:
            raise Exception("Cannot add student to a class more than once.")

        self._students.append(student)

        if len(self._students) > 33:
            warning = f"{self._name} has more than 33 students."
            Classroom.warnings.append(warning)
    
    def remove_student(self, student: "Student") -> None:
        self._students.remove(student)
    
    def get_students(self) -> List["Student"]:
        return self._students


class Person:
    def __init__(self, first_name: str, last_name: str, DOB: datetime.datetime, email: str=None):
        self._first_name = first_name
        self._last_name = last_name
        self._DOB = DOB
        self._email = email
    
    def set_first_name(self, value: str) -> None:
        self._first_name = value
    
    def get_first_name(self):
        return self._first_name
    
    def set_last_name(self, value: str) -> None:
        self._last_name = value
    
    def get_last_name(self) -> str:
        return self._last_name
    
    def set_email(self, value: str) -> None:
        self._email = value
    
    def get_email(self) -> Optional[str]:
        return self._email
    
    def get_DOB(self) -> datetime.datetime:
        return self._DOB
    
    def get_age(self) -> int:
        now = datetime.datetime.now()
        return now.year - self._DOB.year
    
    def greet(self) -> str:
        return f"Hello, my name is {self._first_name} {self._last_name}."
    

class Student(Person):
    def __init__(self, first_name: str, last_name: str, DOB: datetime.datetime, student_number: int, email: str=None):
        super().__init__(first_name, last_name, DOB, email)
        self._student_number = student_number
        self._email_k12 = self._generate_email_k12()
    
    def _generate_email_k12(self) -> str:
        graduation_year = (self._DOB.year + 18) % 100
        return "{}.{}{}@ycdsbk12.ca".format(self._first_name.lower(), self._last_name.lower(), graduation_year)
    
    def set_student_number(self, value: int) -> None:
        try:
            self._student_number = int(value)
        except ValueError:
            raise TypeError("Student number must be an integer.")
        
    
    def get_student_number(self) -> int:
        return self._student_number
        
    def greet(self) -> str:
        return f"Hello, my name is {self._first_name} {self._last_name} and I'm a student."


class Teacher(Person):
    def __init__(self, first_name: str, last_name: str, DOB: datetime.datetime, OCT_PIN: int, email: str=None):
        super().__init__(first_name, last_name, DOB, email)
        self._OCT_PIN = OCT_PIN
        self._classes: List[Classroom] = []
        self._school: Optional[str] = None
        self._email_k12 = self._generate_email_k12()

    def _generate_email_k12(self) -> str:
        return "{}.{}@ycdsb.ca".format(self._first_name.lower(), self._last_name.lower())
    
    def set_OCT_PIN(self, value: int) -> None:
        self._OCT_PIN = value
    
    def get_OCT_PIN(self) -> int:
        return self._OCT_PIN
    
    def set_school(self, value: str) -> None:
        self._school = value
    
    def get_school(self) -> Optional[str]:
        return self._school
    
    def add_class(self, class_: Classroom) -> None:
        if len(self._classes) >= 6:
            raise Exception("A teacher cannot have more than six classes.")
            
        if class_ in self._classes:
            raise Exception("Cannot add the same class twice.")
        
        self._classes.append(class_)
    
    def remove_class(self, class_: Classroom) -> None:
        self._classes.remove(class_)
    
    def get_classes(self) -> List[Classroom]:
        return self._classes
    
    def assign_work(self, class_: Classroom) -> str:
        if class_ not in self._classes:
            raise Exception("Cannot assign work to a class not in a Teacher's classes list.")
        return f"{self._first_name} {self._last_name} assigns work to {class_.get_name()} class."
    
    def greet(self) -> str:
        return f"Hello, my name is {self._first_name} {self._last_name} and I'm a teacher."

def main():
    pass

if __name__ == "__main__" :
    import os
    os.system("pip install -r requirements.txt -q")
    os.system("mypy main.py --disallow-incomplete-defs")  # comment out if needed
    # os.system("pycodestyle main.py") # doesnt work
    os.system("pytest")  # comment out if needed
    main()
