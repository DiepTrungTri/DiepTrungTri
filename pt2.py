# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 06:46:03 2024

@author: abc
"""
import math
# Giải phương trình ax^2 + bx + c = 0
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
# Điều kiện giải pt
if(a!=0):
   delta = b**2 - 4*a*c
   if delta < 0:
       print("Phương trình vô nghiệm")
   elif delta == 0:
       x = -b / (2*a)
       print("Phương trình có nghiệm kép x1=x2=",x)
   else:
       x1 = -b - math.sqrt(delta) / (2 * a)
       x2 = -b + math.sqrt(delta) / (2 * a)
       print("Phương trình có hai nghiệm phân biệt x1={0},x2={1}".format(x1,x2))
       
else:
    print("Phương trình vô nghiệm")