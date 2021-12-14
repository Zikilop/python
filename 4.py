def my_func(x, y):
    if x == 0:
        return "ERROR"
    res = 1
    for i in range(abs(y)):
        res *= x
    return 1/res

print(my_func(float(input("x = ")), int(input("y = "))))
