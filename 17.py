# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:33:26 2024

@author: abc
"""

# Bài 17
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
if a > b and a > c:
    print("Số lớn nhất là: {}".format(a))
elif b > a and b > c:
    print("Số lớn nhất là: {}".format(b))
else:
    print("Số lớn nhất là: {}".format(c))