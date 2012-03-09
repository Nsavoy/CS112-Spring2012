#!/usr/bin/env python

"""
HERPDERP OBJECTS
"""


class Student(object):# capital S is used to denote class.
    def __init__(self, name = "Jane Doe"):#the constructor
        self.name = name

    def say(self, message):
        print self.name + ": " + message

    def say_to(self, other, message):
        self.say(message + ", " + other.name)

    def printMe(self):
        print self.name

class Course(object):
    def __init__(self, name):
        self.name = name
        self.enrolled = []

    def enroll(self, student):
        self.enrolled.append(student)
    
    def printMe(self):
        for student in self.enrolled:
            student.printMe()


bob = Student("Bob")

fred = Student()

bob2 = bob
print bob2 is bob

cs112 = Course("cs112")
cs112.enroll(bob)
cs112.enroll(fred)
cs112.printMe()


bob.say_to(fred, "Hi")
fred.say_to(bob, "Bugger off")
