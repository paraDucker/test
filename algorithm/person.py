# -*- coding:utf-8 -*-
# developTime: 2025/12/1 19:12
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s在吃饭" % self.name)

    def drink(self):
        print("%s在喝酒" % self.name)

    def work(self):
        print("%s在工作" % self.name)
