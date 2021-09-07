class Student:
    def __init__(self, name, age,clas):
        self.name = name
        self.age = age
        self.clas = clas

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_clas(self):
        return self.clas

    def set_age(self, age):
        self.age = age

    def set_name(self,name):
        self.name = name

    def set_clas(self, clas):
        self.clas = clas


class Course:
    def __init__(self, name, code, student_len):
        self.name = name
        self.code = code
        self.studet_len = student_len
        self.studets = []

    def get_course_name(self):
        return self.name

    def get_course_code(self):
        return self.code

    def add_student(self, Student):
        if len(self.studets) < self.studet_len:
            self.studets.append(Student)
            return self.studets
        return len(self.studets)



