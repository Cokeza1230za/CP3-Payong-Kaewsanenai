from tkinter import *
import math


def leftClickButton(event):
    bmi = float(textboxWeight.get()) / math.pow(float(textboxHeight.get()) / 100, 2)
    lableResult.configure(text=int(bmi))


MainWindow = Tk()
lableHeight = Label(MainWindow, text="ส่วนสูง(cm.)").grid(row=0, column=0)
textboxHeight = Entry(MainWindow)
textboxHeight.grid(row=0, column=1)
lableWeight = Label(MainWindow, text="น้ำหนัก(Kg.)").grid(row=1, column=0)
textboxWeight = Entry(MainWindow)
textboxWeight.grid(row=1, column=1)
calculateButton = Button(MainWindow, text="คำนวณ")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2, column=0)
lableResult = Label(MainWindow, text="ผลลัพธ์")
lableResult.grid(row=2, column=1)

MainWindow.mainloop()
