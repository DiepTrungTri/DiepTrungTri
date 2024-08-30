# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:33:26 2024

@author: abc
"""

# Bài 19
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
d = int(input("Nhập số nguyên d: "))
if a < b and a < c and a < d:
    print("Số bé nhất là: {}".format(a))
elif b < a and b < c and b < d:
    print("Số bé nhất là: {}".format(b))
elif c < a and c < b and c < d:
    print("Số bé nhất là: {}".format(c))
else:
    print("Số bé nhất là: {}".format(d))