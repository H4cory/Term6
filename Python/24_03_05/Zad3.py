# 3.	Създайте клас Person с атрибути: име и възраст.
# 3.1.	Създайте метод display(), който показва името и
#  възрастта на обект, създаден чрез класа Person.

# 3.2.	Създайте производен клас Student, който има атрибут
#  faculty.

# 3.3.	Създайте метод displayStudent(), който показва името,
#  възрастта и факултета на обект, създаден чрез класа Student.

# 3.4.	Създайте обект на ученик чрез инстанция в класа Student
#  и след това тествайте метода displayStudent.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
    


class Student(Person):

    def __init__(self, faculty, name, age):
        super().__init__(name, age)
        self.faculty = faculty
    
    def displayStudent(self):
        super().display()
        print(f"Faculty: {self.faculty}")


stud1 = Student("FPNO", "Ivan", 85)
stud1.displayStudent()