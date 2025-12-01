# -*- coding:utf-8 -*-
# developTime: 2025/12/1 19:40
from person import Person
from student import Student
class Teacher(Person):
    def __init__(self,age,name,student:Student):
        super().__init__(age,name)
        self.student = student

    def teach(self):
        print("%s老师在教%s"%(self.name,self.student.name))