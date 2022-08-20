def recursive_range(x):
    if x > 0:
        x -= 1
        recursive_range(x)
        print(x)


recursive_range(5)

print()

for i in range(0, 5):
    print(i)
