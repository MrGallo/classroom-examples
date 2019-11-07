# Classes Test Prep
- Create the classes from the UML image below.
- Create a **main function** to showcase all the functionality.
- **Encapsulate** ALL object fields with getters/setters.

Notes
Person:
- make email a default optional parameter in the initializer. Make the default None.
- Do not make a setter for the DOB.

Teacher:
- The assign_work method will just print something out. Include the teacher name and class name.
- Ensure you cannot add more than 6 classes to a Teacher with the add_class method.

Class_:
- Create a class variable, a list of flags or warnings. When a class exceeds 33 students, a warning is created in the Class_ class.
- Raise an error if you attempt to remove a student from a class who wasn't in the class to begin with.

Extend the program
- Create a School class, make modifications to Teacher and Student.
- Create a all_teachers field for the Teachers class. Make @classmethod to search for a teacher by their OCT_PIN. Make another @classmethod to search for a teacher by their last name.

- [Test File](https://github.com/MrGallo/classroom-examples/blob/master/10-classes/05b-test-prep-tests.py)
- [Solution](https://github.com/MrGallo/classroom-examples/blob/master/10-classes/05b-test-prep-solution.py)

![UML](https://github.com/MrGallo/classroom-examples/blob/master/10-classes/images/test-prep-uml.jpg)
