list_ = eval(input())
char = 1
while(char != 0):
    char = int(input())
    for i in range(len(list_)):
        if(char >= list_[i]):
            list_.insert(i, char)
            break
        if(i == len(list_) - 1):
            list_.append(char)
    print(list_)
