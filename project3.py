
class_grades = {
    'علی احمدی': 18.5,
    'زهرا محمدی': 19,
    'رضا کریمی': 17.25,
    'نازنین غفاری': 20
}
name = input("pleas inter your name: ")
if name in class_grades:
    print("نمره:", class_grades[name])
else:
    print("دانشجو یافت نشد")
