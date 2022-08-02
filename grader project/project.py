from tkinter import *

main = Tk()
main.title("Grading Program")
main.geometry("300x200")

label1 = Label(text="Welcome to the Grading Program")
label1.place(x=30, y=15)
label2 = Label(text="Please enter your mark.")
label2.place(x=30, y=50)
label3 = Label(text="Result:")
label3.place(x=30, y=125)

entry1 = Entry()
entry1.place(x=30, y=80)
grade = Entry()
grade.place(x=30, y=155)


def calculate():
    grade.delete(0, "end")
    mark = eval(entry1.get())
    if 94 < mark <= 100:
        grade.insert(END, "You got an A+")
    elif 89 < mark <= 94:
        grade.insert(END, "You got an A")
    elif 84 < mark <= 89:
        grade.insert(END, "You got a B+")
    elif 79 < mark <= 84:
        grade.insert(END, "You got a B")
    elif 74 < mark <= 79:
        grade.insert(END, "You got a C+")
    elif 69 < mark <= 74:
        grade.insert(END, "You got a C")
    elif 64 < mark <= 69:
        grade.insert(END, "You got a D+")
    elif 59 < mark <= 64:
        grade.insert(END, "You got a D")
    elif 0 <= mark <= 59:
        grade.insert(END, "You failed.")
    else:
        grade.insert(END, "The number is incorrect.")


calc = Button(text="Calculate", command=calculate)
calc.place(x=200, y=75)
