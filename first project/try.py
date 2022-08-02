while True:
    try:
        x = int(input("enter N: "))
        y = 1/x
    except ValueError:
        print("Error, N must be a number")
    else:
        print("1 /", x, "=", y)
        break
