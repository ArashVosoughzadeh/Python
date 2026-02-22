while True:
    unerinput1 = int (input("pleas enter your num 1 : "))
    unerinput2 = int (input("pleas enter your num 2 : "))
    try:
        print(unerinput1/unerinput2)
    except ZeroDivisionError :
        print("can not divide a number to zero")