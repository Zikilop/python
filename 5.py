spec = "#"
print("Специальный символ = '#'")
res = 0
while(1):
    list_ = list(map(lambda x: int(x) if x != spec else spec, input().split()))
    if list_[-1] == spec:
        res += sum(list_[:-1])
        print(f"Результат суммы: {res}")
        break
    else:
        res += sum(list_)
        print(f"Результат суммы: {res}")
