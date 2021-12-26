with open("1.py") as fd:
    while(1):
        e = str(fd.readline()).split()
        if e == []:
            break
        print(e)
