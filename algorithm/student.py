# -*- coding:utf-8 -*-
# developTime: 2025/12/1 19:12
from person import Person
class Student(Person):
    def __init__(self,age,name,score):
        super().__init__(name,age)
        self.score = score

    def study(self):
        print("%s在学习"%self.name)