# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:33:27 2024

@author: abc
"""

# Bài 23 
import math
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c:"))
delta = b**2 - 4*a*c
if delta == 0:
    print("Phương trình có nghiệm kép x = {}".format(-b/(2*a)))
elif delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(x1,x2)
else:
    print("Phương trình vô nghiệm")