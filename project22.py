num1 = int(input("عدد اول را وارد کنید: "))
num2 = int(input("عدد دوم را وارد کنید: "))
num3 = int(input("عدد سوم را وارد کنید: "))

if num1 >= num2 and num1 >= num3:
    print("بزرگ‌ترین عدد:", num1)
elif num2 >= num1 and num2 >= num3:
    print("بزرگ‌ترین عدد:", num2)
else:
    print("بزرگ‌ترین عدد:", num3)