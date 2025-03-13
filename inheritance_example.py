'''
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic animal sound"

# Child class (inherits from Animal)
# The child classes use the same __init__ arguments as the parent class
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Child class (inherits from Animal)
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Creating instances of the child classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Create an instance of the parent class
randy = Animal("Randy")

print(dog.name, "says", dog.make_sound())  # Output: Buddy says Woof!
print(cat.name, "says", cat.make_sound())  # Output: Whiskers says Meow! 
print(randy.name, "says", randy.make_sound())  # Output:  Randy says Some generic animal sound
'''

'''
The next example shows how to create child classes with different (additional)
initalizer parameters from the parent. 
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

# Child class with additional attributes
class Student(Person):
    def __init__(self, name, age, student_id, major):
        # Call the parent class's constructor using super()
        super().__init__(name, age)  
        
        # Add new attributes specific to Student
        self.student_id = student_id
        self.major = major

    def get_grade(self):
        print("\n\n")
        self.grade = float(input(f"Enter a grade for {self.name}: "))
        return(f"{self.name} has a final grade  of {self.grade}")

    # def introduce(self):
       # return super().introduce() + f" I am a {self.major} major with student ID {self.student_id}."

# Creating an instance of Student
student = Student("Alice", 20, "S12345", "Computer Science")
print(student.introduce())
print()
print(student.get_grade())
# Create a person object
person = Person("Anthony", 17)
print(person.introduce())





