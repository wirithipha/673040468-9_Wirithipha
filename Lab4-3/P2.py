# Name: Wirithipha Duangjan
# Student ID: 673040468-9

from datetime import datetime


# Base class
class Person:
    running_id = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._id = self.__create_id()

        self._birthdate = None
        self.__bloodgroup = None
        self.__is_married = False

    def __create_id(self):
        year = datetime.now().year
        pid = str(year) + str(Person.running_id)
        Person.running_id += 1
        return pid

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("ID:", self._id)


# Level 2 : Staff
class Staff(Person):
    def __init__(self, name, age, department, start_year):
        super().__init__(name, age)
        self.department = department
        self.start_year = start_year
        self.tenure_year = datetime.now().year - start_year
        self.__salary = 0

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def display_info(self):
        super().display_info()
        print("Department:", self.department)
        print("Tenure:", self.tenure_year)
        print("Salary:", self.__salary)


# Level 2 : Student
class Student(Person):
    def __init__(self, name, age, start_year, major, level):
        super().__init__(name, age)
        self.start_year = start_year
        self.major = major
        self.level = level
        self.grade_list = []
        self.gpa = 0
        self.__graduation_year = self.__calc_graduation_year()

    def add_grade(self, credit, grade):
        self.grade_list.append((credit, grade))
        self.calculate_gpa()

    def calculate_gpa(self):
        total_credit = 0
        total_point = 0

        for credit, grade in self.grade_list:
            total_credit += credit
            if grade == "A":
                total_point += credit * 4
            elif grade == "B":
                total_point += credit * 3
            elif grade == "C":
                total_point += credit * 2
            elif grade == "D":
                total_point += credit * 1

        if total_credit > 0:
            self.gpa = round(total_point / total_credit, 2)

    def __calc_graduation_year(self):
        if self.level == "undergraduate":
            return self.start_year + 4
        return self.start_year + 2

    def display_info(self):
        super().display_info()
        print("Major:", self.major)
        print("Level:", self.level)
        print("GPA:", self.gpa)
        print("Graduation:", self.__graduation_year)


# Level 3 : Professor
class Professor(Staff):
    def __init__(self, name, age, department, start_year, level, admin=0):
        super().__init__(name, age, department, start_year)
        self.prof_level = level
        self.admin = admin
        self.set_salary()

    def set_salary(self):
        salary = 30000 + self.tenure_year * 1000 + self.prof_level * 10000
        if self.admin == 1:
            salary += 10000
        super().set_salary(salary)

    def display_info(self):
        super().display_info()
        print("Professor level:", self.prof_level)
        print("Admin:", self.admin)


# Level 3 : Undergraduate
class UndergraduateStudent(Student):
    def __init__(self, name, age, start_year, major):
        super().__init__(name, age, start_year, major, "undergraduate")
        self.course_list = []

    def register_course(self, course):
        self.course_list.append(course)

    def display_info(self):
        super().display_info()
        print("Courses:")
        if len(self.course_list) == 0:
            print("(no course)")
        else:
            for c in self.course_list:
                print("-", c)


# Test Program
if __name__ == "__main__":
    # ---- Professor ----
    print("=== Professor ===")
    p = Professor("Dr.A", 45, "CS", 2015, 2, 1)
    p.display_info()

    print("\n----------\n")

    # ---- Undergraduate Student ----
    print("=== Undergraduate Student ===")
    u = UndergraduateStudent("Tom", 20, 2023, "Engineering")
    u.add_grade(3, "A")
    u.add_grade(3, "B")
    u.register_course("OOP")
    u.register_course("Data Structure")
    u.display_info()
