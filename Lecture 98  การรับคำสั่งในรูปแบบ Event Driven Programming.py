from tkinter import *


def leftClickButton(event):
    print("Left Click!!")


def RightClickButton(event):
    print("Right Click!!")


def DoubleClickButton(event):
    print("Double Click!!")


def leftClickButton(event):
    print("Left Click!!")


def RightClickButton(event):
    print("Right Click!!")


def DoubleClickButton(event):
    print("Double Click!!")


MainWindow = Tk()
lableHeight = Label(MainWindow, text="ส่วนสูง(cm.)").grid(row=0, column=0)
textboxHeight = Entry(MainWindow)
textboxHeight.grid(row=0, column=1)
lableWeight = Label(MainWindow, text="น้ำหนัก(Kg.)").grid(row=1, column=0)
textboxWeight = Entry(MainWindow)
textboxWeight.grid(row=1, column=1)
calculateButton = Button(MainWindow,text="คำนวณสิไอน้อง")
calculateButton.grid(row=2)
MainWindow.mainloop()
