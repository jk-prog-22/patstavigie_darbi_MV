sum = 0
skaitlis = 0

while True:
    ievade = int(input("Ievadi skaitli: "))
    if ievade == 0:
        break

    if ievade % 2 == 0:
        sum = sum + ievade
        skaitlis = skaitlis + 1

if skaitlis > 0:
    print("Vidējais no pāra skaitļiem:", sum / skaitlis)
else:
    print("Netika ievadīts neviens pāra skaitlis")

