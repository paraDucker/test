# -*- coding:utf-8 -*-
# developTime: 2025/12/1 19:12
from person import Person
from teacher import Teacher
class Student(Person):
    def __init__(self,age,name,score,teacher:Teacher):
        super().__init__(name,age)
        self.score = score
        self.teacher = teacher

    def study(self):
        print("%s在学习"%self.name)

    def play(self):
        print("%s在")

    def celebrate(self,gift):
        print("%s同学给%s准备了%s"%(self.name,self.teacher.name,gift))