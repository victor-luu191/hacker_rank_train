import math


class Rectangle:
    def __int__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * self.radius ** 2
