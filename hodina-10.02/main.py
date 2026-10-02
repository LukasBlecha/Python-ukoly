x = -5

# příkaz větvení
if x>=0:
    if x>0:
        print(f"{x} je kladné číslo nebo nula")
    else:
        print(f"{x} je nula")
else:
    print(f"{x} je záporné číslo")
    x= -x
print(f"absolutní hodnota: {x}")

