def div_num(num_1, num_2):
    return num_1/num_2 if num_2 != 0 else "ERROR"

num_1, num_2 = float(input("Делимое = ")), float(input("Делитель = "))
print(div_num(num_1, num_2))
