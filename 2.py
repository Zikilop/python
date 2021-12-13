list_ = eval(input())
for i, _ in enumerate(list_[1::2]):
    list_[2*i + 1], list_[2*i] = list_[2*i], list_[2*i + 1]
print(list_)
