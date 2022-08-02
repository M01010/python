import os
os.chdir("c:/Users/R-tro/Desktop/projects/Python/first project")
with open(r"./Example1.txt", "r") as readfile:
    with open(r"./Example3", "w") as writefile:
        for i in readfile:
            writefile.write(i)
