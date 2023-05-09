from tkinter import *
import math

def leftClickButton(event):
    bmi = (float(textboxWeight.get()) / math.pow(float(textboxHeight.get()) / 100, 2))
    lableResult.configure(text=int(bmi))
    if bmi >= 30.0:
        result_text = 'อ้วนมาก'
    elif bmi >= 25.0:
        result_text = 'อ้วน'
    elif bmi >= 23.0:
        result_text = 'น้ำหนักเกิน'
    elif bmi >= 18.6:
        result_text = 'น้ำหนักปกติเหมาะสม'
    else:
        result_text = 'ผอมเกินไป'
    lableResult2.configure(text=result_text)

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
lableResult = Label(MainWindow, text="BMI")
lableResult.grid(row=2, column=1)
lableResult2 = Label(MainWindow, text="")
lableResult2.grid(row=3, column=1)

MainWindow.mainloop()
