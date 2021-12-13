gain, cost = int(input("Выручка = ")), int(input("Издрежки = "))
val = gain - cost
if(val > 0):
    print(f"Прибыль!\nРентабельность выручки = {val/gain}")
    num = int(input("Число сотрудников = "))
    print(f"Прибыль фирмы в расчёте на одного сотрудника = {val/num}")
elif(val < 0):
    print("Убыток!")
else:
    print("404")
