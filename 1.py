with open("1_output.txt", "w") as fd:
    inp = input()
    while(inp != ""):
        fd.write(inp + '\n')
        inp = input()
