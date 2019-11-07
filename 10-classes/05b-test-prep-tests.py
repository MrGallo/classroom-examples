import datetime

import pytest

from main import Classroom, Person, Student, Teacher



def test_classroom_hidden_fields():
    math = Classroom("Math")
    assert math._name == "Math"
    assert math._students == []


def test_classroom_getters_setters():
    math = Classroom("Math")

    assert math.get_students() == []
    assert math.get_name() == "Math"

    math.set_name("Blah")
    assert math.get_name() == "Blah"


def test_classroom_add_remove_student():
    class StudentMock:
        pass


    math = Classroom("Math")

    some_student = StudentMock()
    math.add_student(some_student)
    assert len(math.get_students()) == 1

    math.remove_student(some_student)
    assert math.get_students() == []

    # Raises some exception when removing a studentnot in the class.
    with pytest.raises(Exception):
        math.remove_student(some_student)
    

    # Raise an exception when the same student is added to the same class
    math.add_student(some_student)
    with pytest.raises(Exception):
        math.add_student(some_student)


def test_classroom_warnings():
    assert Classroom.warnings == []

    some_class = Classroom("Math")

    # add 34 students to the class
    for i in range(34):
        some_student = Student("blah", "blah", datetime.datetime.now(), i)
        some_class.add_student(some_student)
    
    # should add a warning to the class variable 'warnings'
    warning_string = Classroom.warnings[0]
    assert warning_string == "Math has more than 33 students."


def test_person_init():
    person = Person("John", "Smith", datetime.datetime(2019, 1, 1))
    assert person._first_name == "John"
    assert person._last_name == "Smith"
    assert person._DOB == datetime.datetime(2019, 1, 1)
    assert person._email is None

    # test optional email
    person = Person("John", "Smith", datetime.datetime(2019, 1, 1), "test@test.com")
    assert person._email == "test@test.com"


def test_person_greet():
    person = Person("John", "Smith", datetime.datetime(2019, 1, 1))
    assert person.greet() == "Hello, my name is John Smith."

    person = Person("Blah", "Test", datetime.datetime(2019, 1, 1))
    assert person.greet() == "Hello, my name is Blah Test."


def test_person_setters_getters():
    person = Person("John", "Smith", datetime.datetime(2019, 1, 1), "test@test.com")
    
    person.set_first_name("Johnny")
    assert person.get_first_name() == "Johnny"

    person.set_last_name("Smithly")
    assert person.get_last_name() == "Smithly"

    person.set_email("blah@blah.com")
    person.get_email() == "blah@blah.com"

    # cannot set DOB
    with pytest.raises(AttributeError):
        person.set_DOB(datetime.datetime.now())
    
    person.get_DOB() == datetime.datetime(2019, 1, 1)


def test_person_get_age():
    now = datetime.datetime.now()
    person = Person("", "", datetime.datetime(now.year, 1, 1))
    assert person.get_age() == 0

    person = Person("", "", datetime.datetime(now.year-1, 1, 1))
    assert person.get_age() == 1

    person = Person("", "", datetime.datetime(now.year-5, 1, 1))
    assert person.get_age() == 5


def test_student_init():
    student = Student("first", "last", datetime.datetime(2002, 1, 1), 1234)
    assert isinstance(student, Person)
    assert student._first_name == "first"
    assert student._last_name == "last"
    assert student._DOB == datetime.datetime(2002, 1, 1)
    assert student._student_number == 1234
    assert student._email == None
    assert student._email_k12 == "first.last20@ycdsbk12.ca"


def test_generate_email():
    student = Student("first", "last", datetime.datetime(2020, 1, 1), 1234)
    assert student._email_k12 == "first.last38@ycdsbk12.ca"

    student = Student("John", "Smith", datetime.datetime(2020, 1, 1), 1234)
    assert student._email_k12 == "john.smith38@ycdsbk12.ca"

def test_student_getters_setters():
    student = Student("first", "last", datetime.datetime(2020, 1, 1), 1234)
    
    student.set_first_name("John")
    assert student.get_first_name() == "John"

    student.set_last_name("Smith")
    assert student.get_last_name() == "Smith"

    student.set_student_number(4321)
    assert student.get_student_number() == 4321


def test_student_greet():
    student = Student("first", "last", datetime.datetime(2020, 1, 1), 1234)
    assert student.greet() == "Hello, my name is first last and I'm a student."

    student = Student("John", "Smith", datetime.datetime(2020, 1, 1), 1234)
    assert student.greet() == "Hello, my name is John Smith and I'm a student."


def test_teacher_init():
    teacher = Teacher("John", "Smith", datetime.datetime(2020, 1, 1), 1234)
    assert isinstance(teacher, Person)
    assert teacher._OCT_PIN == 1234
    assert teacher._email_k12 == "john.smith@ycdsb.ca"
    assert teacher._classes == []

def test_teacher_getters_setters():
    teacher = Teacher("John", "Smith", datetime.datetime(2020, 1, 1), 1234)
    assert teacher.get_first_name() == "John"

    teacher.set_OCT_PIN(5432)
    assert teacher.get_OCT_PIN() == 5432

    teacher.set_school("St. Joan")
    assert teacher.get_school() == "St. Joan"

def test_teacher_add_remove_class():
    teacher = Teacher("John", "Smith", datetime.datetime(2020, 1, 1), 1234)
    some_class = Classroom("Math")
    teacher.add_class(some_class)

    assert some_class in teacher.get_classes()

    teacher.remove_class(some_class)
    assert teacher.get_classes() == []

    # ensure you cannot teach the same class twice
    teacher.add_class(some_class)
    with pytest.raises(Exception):
        teacher.add_class(some_class)

def test_teacher_cannot_have_more_than_6_classes():
    teacher = Teacher("John", "Smith", datetime.datetime(2020, 1, 1), 1234)

    # OK to have 6
    for i in range(6):
        some_class = Classroom(str(i))
        teacher.add_class(some_class)
    
    # Error when trying to add a 7th class
    with pytest.raises(Exception):
        one_too_many = Classroom("Cant teach this")
        teacher.add_class(one_too_many)
    
    assert len(teacher.get_classes()) == 6


def test_teacher_assing_work():
    teacher = Teacher("John", "Smith", datetime.datetime(2020, 1, 1), 1234)
    math = Classroom("Math")
    teacher.add_class(math)

    assert teacher.assign_work(math) == "John Smith assigns work to Math class."

def test_teacher_greet():
    teacher = Teacher("John", "Smith", datetime.datetime(2020, 1, 1), 1234)
    assert teacher.greet() == "Hello, my name is John Smith and I'm a teacher."



# EXTRA TESTS
@pytest.mark.skip
def test_set_student_number_raises_error_with_invalid_value():
    student = Student("first", "last", datetime.datetime(2020, 1, 1), 1234)
    
    with pytest.raises(TypeError):
        student.set_student_number("abc123")


@pytest.mark.skip
def test_cant_assign_work_to_someone_elses_class():
    teacher = Teacher("John", "Smith", datetime.datetime(2020, 1, 1), 1234)
    
    # raise an error if assigning work to a class not taught by the teacher
    someone_elses_class = Classroom("Computer Studies")
    with pytest.raises(Exception):
        teacher.assign_work(someone_elses_class)
