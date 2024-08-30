# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:33:24 2024

@author: abc
"""

# Bài 7
import math
radius = float(input("Nhập vào bán kính hình tròn: "))
chuvi = 2 * math.pi * radius
dientich = math.pi * (radius**2)
print("Chu vi là: ",round(chuvi,2))
print("Diện tích là: ",round(dientich,2))