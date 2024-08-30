# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:33:27 2024

@author: abc
"""

# Bài 20
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
if a > b and a > c:
    print("Số lớn nhất là:{}".format(a))
elif b > a and b > c:
    print("Số lớn nhất là: {}".format(b))
else:
    print("Số lớn nhất là: {}".format(c))