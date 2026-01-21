class Student:
    def __init__(self, name: str, age: int, grade: int):
        self.name = name
        self.age = age
        self.grade = grade
        
    def info(self):
        print(f"{self.name}, {self.age} yoshda, {self.grade}-kurs talabasi.")
        
        
s1 = Student("ali", 18, 5)
s2 = Student("vali", 19, 3)
s3 = Student("soli", 19, 5)
s4 = Student("sami", 21, 5)
s5 = Student("g'ani", 24, 5)

students = [s1, s2, s3, s4, s5]

max_user = max(students, key=lambda x: x.age)
max_user.info()
