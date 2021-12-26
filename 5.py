with open('5_out.txt', "w") as fd:
    for i in range(10):
        fd.write(str(i) + ' ')
with open('5_out.txt') as fd:
    text = fd.readlines()
    print(sum(list(map(int, text[0].split()))))
