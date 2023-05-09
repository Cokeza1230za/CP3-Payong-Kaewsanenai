from tkinter import *


def SayHello():
    print("หวัดดีไอน้อง")


MainWindow = Tk()
button = Button(MainWindow, text="Click me1!!!", command=SayHello).grid(row=2, column=1)
button2 = Button(MainWindow, text="Click me2!!!", command=SayHello).grid(row=1, column=1)
button3 = Button(MainWindow, text="Click me3!!!", command=SayHello).grid(row=0, column=0)
lable = Label(text="ดีจั๊ฟไอน้อง",width=20,fg="red",bg="#000fff000",font=("Angsana new",80)).grid(row=0,column=1)
MainWindow.mainloop()
