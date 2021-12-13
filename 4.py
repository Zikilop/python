n = int(input())
max_ = 0
while(n):
    max_ = n % 10 if (n % 10) > max_ else max_
    n //= 10
print(max_)
