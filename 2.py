with open("2_test.txt") as fd:
    text = fd.readlines()
    print(f"Количество строк = {len(text)}")
    for i, el in enumerate(text):
        print(f"Количество слов в {i} строке = {len(el.split())}")
