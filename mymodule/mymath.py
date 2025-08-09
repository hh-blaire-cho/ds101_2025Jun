import numpy as np

class MyMath:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.age = "14"
        self.color = "Blue"
    
    def is_bigger_than(self, a):
        if self.number > a:
            return True
        return False
    
    def is_smaller_than(self, a):
        if self.number < a:
            return True
        return False

    def average(self, lst):
        return sum(lst)/len(lst)


# print(arr.color) # error
# print(x1.shape) # error
