dict_ = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("4_in.txt") as fd:
    text = fd.readlines()
    with open("4_out.txt", "w") as fd2:
        for st in text:
            temp = st.split()
            print(f"{dict_[temp[0]]} " + " ".join(temp[1:]), file=fd2)

