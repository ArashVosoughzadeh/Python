number = {"a": 5,"b": 12, "c": 7, "d": 4}

filteR = {}
for key, value in number.items():
    if value % 2 != 0:
        filteR[key] = value

print(filteR)
