c = int(input("لطفا تعداد دانش اموزان را وارد کنید : "))
total = 0
while c >= 0: 
    score=float(input("Nomereh : "))
    total += score
    c-=1


print("Averege", total/c)
