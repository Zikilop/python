cal = {(12, 1, 2) : "Зима", (3, 4, 5) : "Весна", (6, 7, 8) : "Лето", (9, 10, 11) : "Осень"}
n = int(input())
for key in cal:
    if n in key:
        print(cal[key])
