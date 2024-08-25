# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 11:05:12 2024

@author: abc
"""

# Bài 2 chuyển chuỗi
a = "I'm a cat"
print(a.capitalize())
print(a.title())
print(a.upper())
a_transformed = a[0].lower() + a[1:3].upper() + a[3:5] + a[5:].upper()
print(a_transformed)