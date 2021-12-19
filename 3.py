def my_func(a, b, c):
    temp = [a, b, c]
    return sum(temp) - min(temp)

print(my_func(float(input("a = ")), float(input("b = ")), float(input("c = "))))

