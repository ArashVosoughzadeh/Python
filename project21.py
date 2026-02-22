
weight = float(input("وزن خود را به کیلوگرم وارد کنید: "))
height = float(input("قد خود را به متر وارد کنید: "))

bmi = weight / (height **2)

print(" BMI شما:", round(bmi, 2))

if bmi < 18.5:
    print("شما لاغر هستید.")
elif bmi >= 18.5 and bmi < 25:
    print("وزن شما نرمال است.")
elif bmi >= 25 and bmi < 30:
    print("شما اضافه وزن دارید.")
else:
    print("شما چاق هستید.")
