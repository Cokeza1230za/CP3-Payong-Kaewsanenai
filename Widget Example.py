from tkinter import *


def SayHello():
    print("หวัดดีไอน้อง")


MainWindow = Tk()
button = Button(MainWindow, text="Click me1!!!", command=SayHello).grid(row=0,column=0)
button2 = Button(MainWindow, text="Click me2!!!", command=SayHello).grid(row=0,column=1)
button3 = Button(MainWindow, text="Click me3!!!", command=SayHello).grid(row=2,column=0)

MainWindow.mainloop()
