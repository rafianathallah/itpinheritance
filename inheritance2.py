class Person:
    def __init__(self,name: str,address: str):
        self.name = name
        self.address = address
        
    def get_name(self):
        return self.name
    def get_address(self):
        return self.address
    
    def set_address(self, address):
        self.address = address
        
    def sentence(self):
        return f'Name: {self.name}\nAddress: {self.address}'
    
class Student(Person):
    def __init__(self,name: str, address: str):
        Person.__init__(self,name,address)
        self.course_grade = {}
        self.total = 0
        self.num_courses = 0
        
    def sentence(self):
        return f'{Person.sentence(self)}'
    
    def add_course_grade(self,course: str,grade: int):
        self.course = course
        self.grade = grade
        self.course_grade.update({course: grade})
        self.num_courses = len(self.course_grade)
    
    def print_grades(self):
        for i in self.course_grade:
            print(f'{i}: {self.course_grade[i]}')
            
    def get_average(self):
        for i in self.course_grade.values():
            self.total += i
        self.average = self.total / len(self.course_grade)
        return self.average

class Teacher(Person):
    def __init__(self,name: str,address: str):
        Person.__init__(self,name,address)
        self.courses = []
        self.num_courses = 0
    
    def sentence(self):
        return f'{Person.sentence(self)}'
    
    def add_course(self, course):
        if course in self.courses:
            return False
        else:
            self.courses.append(course)
            self.num_courses = len(self.courses)
            return True
    def remove_course(self, course):
        if course not in self.courses:
            return False
        else:
            self.courses.remove(course)
            self.num_courses = len(self.courses)
            return True
        
def test():
    student1 = Student("Me", "Bekasi")
    print(student1.sentence())
    student1.add_course_grade("English", 98)
    student1.add_course_grade("Math", 90)
    student1.add_course_grade("Indonesian", 85)
    student1.add_course_grade("Science", 88)
    student1.print_grades()
    print("Average:",student1.get_average())
    
    teacher1 = Teacher("sensei", "their house")
    print(teacher1.sentence)
    teacher1.add_course("English")
    teacher1.add_course("Math")
    teacher1.add_course("Indonesian")
    teacher1.add_course("Science")
    teacher1.remove_course("Science")

test()