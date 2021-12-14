list_ = eval(input())
res = [item for i, item in enumerate(list_[1:]) if list_[i + 1] > list_[i]]
print(res)
