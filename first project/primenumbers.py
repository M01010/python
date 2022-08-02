primenumbers = set()
x = 100
for i in range(2, x+1):
    primenumbers.add(i)

for number in primenumbers:
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        print(number, end=" ")
