# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 08:58:35 2024

@author: abc
"""

# Xét a,b,c là cạnh tam 
a, b, c = map(float,input("Nhập a, b, c: ").split())
# Điều kiện
if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
    print("{}, {}, {}, là cạnh của tam giác".format(a,b,c))
else:
    print("{}, {}, {}, không là cạnh của tam giác".format(a,b,c))