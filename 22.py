# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:33:27 2024

@author: abc
"""

# Bài 22
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
if a!= 0:
    x = -b/a
    print("Phương trình có nghiệm x là {}".format(x))
elif a == 0 and b == 0:
    print("Phương trình có vô số nghiệm")
else:
    print("Phương trình vô nghiệm")