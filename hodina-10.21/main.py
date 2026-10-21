
a = int(input("Zadej  1. číslo :"))
b = int(input("Zadej  2. číslo :"))
c = int(input("Zadej  3. číslo :"))

min = a
max = a

if b < min:
   min = b
elif b > max:
   max = b
if c < min:
   min = c
elif c > max:
   max = c

print(f"Minimum: {min}\nMaximum: {max}")