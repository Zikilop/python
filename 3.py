NUM = 20
with open("3_test.txt") as fd:
    text = fd.readlines()
    mean = 0.
    print("Имеют оклад меньше 20 тыс.")
    for el in text:
        el_parse = el.split()
        mean += float(el_parse[1])
        if(float(el_parse[1]) < NUM):
            print(f"{el_parse[0]} имеет меньше 20 тыс.")
print(f"Средняя величина дохода = {mean/len(text)}")
