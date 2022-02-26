gasamount = float(input("Gazes pateriņš, kWh: "))
tarifs1 = 0.1045819
tarifs2 = 0.0548696
tarifs3 = 0.0394548
tarifs4 = 0.0487234
if gasamount <= 2635:
    print("Gazes cena: ", gasamount * tarifs1)
elif gasamount <= 5269:
    print("Gazes cena: ", gasamount * tarifs1)
elif gasamount <= 63227.9:
    print("Gazes cena: ", gasamount * tarifs1)
elif gasamount <= 263450:
    print("Gazes cena: ", gasamount * tarifs1)
else:
    print("Tarifs nav noteikts")