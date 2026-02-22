
num1 = float(input("pleas inter your number: "))

op = input("   + - * / choose: ")

if op == "": 
    print("you dont have any number")
else:
    num2 = float(input("pleas inter number 2:"))

    if op == "+":
        print("نتیجه:", num1 + num2)
    elif op == "-":
        print("نتیجه:", num1 - num2)
    elif op == "*":
        print("نتیجه:", num1 * num2)
    elif op == "/":
        if num2 != 0:
            print("نتیجه:", num1 / num2)
        else:
            print("عدد نداری نادان")
    else:
        print("you dont have a :Choose:")
