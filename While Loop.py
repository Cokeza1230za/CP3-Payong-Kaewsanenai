correctNumber = 5
Usernubmer = 0
while Usernubmer != correctNumber:
    Usernubmer = int(input("ใส่เลขไอน้อง >>"))
    if Usernubmer > correctNumber:
        print("เยอะเกินไอน้อง")
    elif Usernubmer < correctNumber:
        print("น้อยเกินไอน้อง")
    elif Usernubmer == correctNumber:
        print("ถูกต้องไอน้อง")
