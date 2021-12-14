from itertools import count, cycle
n = int(input("Целое число = "))
it1 = count(n, 1)
for i in it1:
    print(i)
    if(i >= n + 10):
        break
list_ = eval(input("Введите список = "))
it2 = cycle(list_)
for i, item in enumerate(it2):
    print(item)
    if(i >= len(list_) + 10):
        break
  
