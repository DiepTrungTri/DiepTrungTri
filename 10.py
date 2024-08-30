# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:33:25 2024

@author: abc
"""

# Bài 10
a = int(input("Số xe thứ nhất: "))
b = int(input("Số xe thứ hai: "))
c = int(input("Số xe thứ ba: "))
d = int(input("Số xe thứ tư: ")) 
a1 = a % 10
b1 = b % 10
c1 = c % 10
d1 = d % 10
tong = a1 + b1 + c1 + d1
tong1 = tong // 10 
tong2 = tong % 10
sonut = tong1 + tong2
print(f"Số nút là {sonut}")