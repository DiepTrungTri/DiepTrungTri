# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:33:23 2024

@author: abc
"""

# Bài 3
a = int(input("Nhập vào a: "))
b = int(input("Nhập vào b: "))
if a > 0 and b > 0:
    phannguyen = a // b
    phandu = a % b 
    print(f"Phần nguyên là {phannguyen}, phần dư là {phandu}")