a, b = float(input()), float(input())
new = a
day = 1
while(new < b):
    new += 0.1*new
    day += 1
print(day)
