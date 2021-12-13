print("Ввод данных")
name = ' '
i = 1
list_ = []
while(True):
    name = input("Название : ")
    if(name == ""):
        break
    cost = input("Цена : ")
    count = input("Количество : ")
    meas = input("ед : ")
    list_.append(tuple([i, {"Название" : name, "Цена" : cost, "Количество" : count, "ед" : meas}]))
    i += 1

print("Конец ввода")
print(list_)

analit = {"Название": [], "Цена" : [], "Количество" : [], "ед" : []}

for item in list_:
    temp = item[1]
    for key, val in temp.items():
        if val not in analit[key]:
            analit[key].append(val)

print(analit)
            
        
