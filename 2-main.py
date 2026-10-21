a = int(input("Zadej  1. číslo :"))
b = int(input("Zadej  2. číslo :"))
c = int(input("Zadej  3. číslo :"))

if a > b:
    p = a
    a = b
    b = p

if b > c:
    p = b
    b = c
    c = p

if a > b:
    p = a
    a = b
    b = p

print(f"{a}<{b}<{c}")



