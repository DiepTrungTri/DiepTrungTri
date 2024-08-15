# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 08:39:50 2024

@author: abc
"""

# Giải phương trình bậc nhất
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
# Điều kiện
if(a !=0):
    x = -b / a
    print("Phương trình có nghiệm",x)
else:
    print("Phương trình vô nghiệm")
    