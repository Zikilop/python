int_func = lambda text: text[0].upper() + text[1:]

print(' '.join(list(map(int_func, input().split()))))
    
