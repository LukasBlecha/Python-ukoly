# *******************************************************
# Denní pozdrav


cas=float(input("Dobrý den, kolik je u tebe hodin?"))


if 6 <= cas <= 10:
    print("Dobré ráno!")
elif 11 <= cas <= 11:
    print("Dopoledne")
elif 12 <= cas <= 12:
    print("Dobré poledne!")
elif 13 <= cas <= 16:
    print("Dobré odpoledne!")
elif 17 <= cas <= 23:
    print("Dobrý večer!")
else:
    print("Dobrou noc!")      