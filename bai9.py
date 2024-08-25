# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:46:28 2024

@author: abc
"""

# Bài 9 
import math
a = float(input("Nhập a: "))
b = float(input("Nhập b:"))
sqrt_a = math.sqrt(a)
sqrt_b = math.sqrt(b)
sqrt_ab = math.sqrt(a * b)

fourth_root_a = a ** (1/4)
fourth_root_b = b ** (1/4)
fourth_root_ab = sqrt_ab ** (1/4)

# Biểu thức tính toán
result = ((sqrt_a - sqrt_b) / (fourth_root_a - fourth_root_b)) - ((sqrt_a + fourth_root_ab) / (fourth_root_a + fourth_root_b))
print(result)