from tkinter import *


def SayHello():
    print("หวัดดีไอน้อง")


MainWindow = Tk()
button = Button(MainWindow, text="Click me!!!", command=SayHello)
button.place(x=65, y=20)
MainWindow.mainloop()
