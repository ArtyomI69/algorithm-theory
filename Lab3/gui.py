import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from console import function

root = Tk()
root.title("Lab3")

# Frames
imageBtnFrame = Frame(root)
imageBtnFrame.grid(row=0, column=0)

inputsFrame = Frame(root)
inputsFrame.grid(row=0, column=1)

tableFrame = Frame(root)
tableFrame.grid(row=1, column=0)

# Image
image = Image.open("formula.jpg")
image = image.resize((300, 100))
photo = ImageTk.PhotoImage(image)

imageLabel = Label(imageBtnFrame, image=photo)
imageLabel.grid(row=0, column=0)


# Button
def function(x):
    if x <= 0:
        return "Функция не существует при данном аргументе"
    else:
        return math.log(x)


def btn_click_handler():
    tree.delete(*tree.get_children())

    try:
        a = float(aInput.get())
    except:
        messagebox.showerror("Ошибка", "a должно быть числом")
        return
    try:
        b = float(bInput.get())
    except:
        messagebox.showerror("Ошибка", "b должно быть числом")
        return
    try:
        h = float(hInput.get())
    except:
        messagebox.showerror("Ошибка", "h должно быть числом")
        return

    x = a
    i = 0
    while x <= b:
        tree.insert("", "end", values=(i, x, function(x)))
        i += 1
        x += h


btn = Button(imageBtnFrame, text="Выполнить", width=42, height=2, command=btn_click_handler)
btn.grid(row=1, column=0)

# Inputs
inputsHeading = Label(inputsFrame, text="Параметры диапазона")
inputsHeading.grid(row=0, column=0)
inputsHeadingValue = Label(inputsFrame, text="")
inputsHeadingValue.grid(row=0, column=1)

aLabel = Label(inputsFrame, text="Начало диапазона(a)")
aLabel.grid(row=1, column=0)
aInput = Entry(inputsFrame, width=20)
aInput.grid(row=1, column=1)

bLabel = Label(inputsFrame, text="Начало диапазона(b)")
bLabel.grid(row=2, column=0)
bInput = Entry(inputsFrame, width=20)
bInput.grid(row=2, column=1)

hLabel = Label(inputsFrame, text="Шаг(h)")
hLabel.grid(row=3, column=0)
hInput = Entry(inputsFrame, width=20)
hInput.grid(row=3, column=1)

formulaLabel = Label(inputsFrame, text="Текущая формула")
formulaLabel.grid(row=4, column=0)
formulaValue = Label(inputsFrame, text="f(x)=ln(x)")
formulaValue.grid(row=4, column=1)

# Table
tree = ttk.Treeview(tableFrame, columns=("iCounter", "functionArg", "functionVal"), show="headings")
tree.configure(height=30)
tree.heading("iCounter", text="№")
tree.heading("functionArg", text="x")
tree.heading("functionVal", text="f(x)")

tree.grid(row=0, column=0)

root.mainloop()
