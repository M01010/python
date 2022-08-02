import os
os.chdir("c:/Users/R-tro/Desktop/projects/Python/first project")
with open(r"./Example1.txt", "r") as file1:
    file_content = file1.read()
    print(file_content)

print(file1.closed)
