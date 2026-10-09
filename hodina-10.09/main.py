x1 = 2
y1 = 1.5
x2 = 6
y2 = 7

# bod (postava)
xb = float(input("Zadej x souřadnici postavy:"))
yb = float(input("Zadej y souřadnici postavy:"))

# test kolize
if xb>=x1 and xb<=x2 and yb>=y1 and yb<=y2:
    print("postava je uvnitř objektu")
else:
    print("postava je mimo objekt")

if xb<x1 or xb>x2 or yb<y1 or yb>y2:
    print("postava je mimo objekt")
else:          
    print("postava je uvnitř objektu")
