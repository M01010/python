with open(r"Example1.txt", "r") as file1:
    for i, x in enumerate(file1):
        print("line: ", i+1, x)
