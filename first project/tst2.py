def cap_space(txt: str) -> str:
    cap = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    txtl = list(txt)
    for i, value in enumerate(txtl):
        if value in cap:
            txtl[i] = value.lower()
            txtl.insert(i, " ")
    txt = ""
    for i in txtl:
        txt += i
    return txt


string = "helloWRld"
print(string)
print(cap_space(string))
