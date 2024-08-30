# Bài 26
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
#a 
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print(f"Thứ tự tăng dần các số là: {a},{b},{c}")
#b
a = int(input("Nhập hàng nghìn a: "))
b = int(input("Nhập hàng trăm b : "))
c = int(input("Nhập hàng chục c: "))
d = int(input("Nhập hàng đơn vị d: "))
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if a > d:
    a, d = d, a
if b > c:
    b, c = c, b
if b > d:
    b, d = d, b
if c > d:
    c, d = d, c
print(f"Số nguyên theo thứ tự tăng dần là: {a}{b}{c}{d}")