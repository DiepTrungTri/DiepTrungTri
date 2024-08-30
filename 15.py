# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:33:26 2024

@author: abc
"""

# Bài 15
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
a1 = ((a + b ) / a**(1/3) + b**(1/3)) - (a * b)**(1/3)
a2 = (a**(1/3) - b**(1/3))**2
kq = a1 / a2
print("Kết quả là: ",round(kq,2))