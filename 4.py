list_ = eval(input())
print([item for i, item in enumerate(list_) if item not in list_[:i] + list_[i+1:]])
