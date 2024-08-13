class Student:
    name = "Sachin"
    age = 20

    def greet(self):
        print("Rahul")
        print(self.name)
# Create an instance of the Student class
student_instance = Student()

# Call the greet method
student_instance.name="Gotam"
print(student_instance.age)
student_instance.greet()

class Person:
    name = "Deepika"
    city = "Mumbai"
    age = 20
    def __how(self):
      print("gungun")
p1 = Person()

p1.age=60
# Check if 'age' exists before deleting
if hasattr(p1, 'age'):
    del p1.age
    print("Attribute 'age' deleted successfully.")
else:
    print("The attribute 'age' does not exist on the instance.")

# Trying to access the attribute after deletion
try:
    print(p1.age)
except AttributeError as e:
    print(e)  # Outputs: 'Person' object has no attribute 'age'

# print(p1.__how())
print(p1.name)
del p1

import keyword

print(keyword.kwlist)  # Prints a list of all Python keywords


class baacha(Student):
    hey="How"


b1=baacha()
b1.greet()