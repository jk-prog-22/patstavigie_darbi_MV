for i in range(1, 100):
    if i % 3 == 0:
        print("Bum,", end=" ")
    elif i % 5 == 0:
        print("Rum,", end=" ")
    elif i % 3 == 0 and i % 5 == 0:
        print("BumRum,", end=" ")
    else:
        print(i, ",", sep="", end=" ")