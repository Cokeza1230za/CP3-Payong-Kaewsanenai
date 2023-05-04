try:
    input1 = int(input("A :"))
    input2 = int(input("B :"))
    print(input1/input2)
except ValueError:
    print("Error : ใส่เลขอย่างเดียวนะไอน้อง ")
except ZeroDivisionError:
    print("Error!! : อย่าใส่เลข 0 ไอน้อง")
except:
    print("Error!!")
