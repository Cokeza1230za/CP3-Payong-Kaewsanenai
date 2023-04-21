# Login และแสดงข้อความต้อนรับพร้อมรายการสินค้า
usernameInput = input("Username :")
passwordInput = input("Password :")

if usernameInput == "cokeza007" and passwordInput == "1234":
    print("Welcome To Coke Shop!!!")
    print("--------------------------")
    print("      Product list")
    print("--------------------------")
    print("1.ปากกา 5 THB")
    print("2.ปากกาลูกลื่น 10 THB")
    print("3.ดินสอ 5 THB")
    print("4.ดินสอกดด้ามไม้ 15 THB ")
    print("5.ยางลบ 8 THB ")
    print("6.ไม้บรรทัด 15 THB ")
    print("7.น้ำยาลบคำผิด 25 THB ")
    print("--------------------------")
    print("0.ยกเลิกรายการที่ทำทั้งหมด *ถ้ายกเลิกคุณต้อง Login เข้าสู่ระบบใหม่")
    print("--------------------------")

    # เลือกสินค้าพร้อมแสดงรายการที่เลือกและบวกราคาสินค้า
    Pen = 1
    BallPointPen = 2
    Pencil = 3
    MechanicalPencil = 4
    Eraser = 5
    Ruler = 6
    CorrectionFliuid = 7
    userSelected1 = int(input("สินค้าที่ต้อการซื้อ>>"))

    if userSelected1 == 1:
        amount = int(input("ใส่จำนวนสินค้า"))
        print("----------Bill------------")
        print("ปากกา", amount, "แท่ง")
        print("ทั้งหมดราคา", 5 * amount, "บาท")
        print("--------------------------")
        print("      ขอบคุณที่ใช้บริการ")
        print("--------------------------")
    elif userSelected1 == 2:
        amount = int(input("ใส่จำนวนสินค้า"))
        print("----------Bill------------")
        print("ปากกาลูกลื่น", amount, "แท่ง")
        print("ทั้งหมดราคา", 10 * amount, "บาท")
        print("--------------------------")
        print("      ขอบคุณที่ใช้บริการ")
        print("--------------------------")
    elif userSelected1 == 3:
        amount = int(input("ใส่จำนวนสินค้า"))
        print("----------Bill------------")
        print("ดินสอ", amount, "แท่ง")
        print("ทั้งหมดราคา", 5 * amount, "บาท")
        print("--------------------------")
        print("      ขอบคุณที่ใช้บริการ")
        print("--------------------------")
    elif userSelected1 == 4:
        amount = int(input("ใส่จำนวนสินค้า"))
        print("----------Bill------------")
        print("ดินสอกดด้ามไม้", amount, "แท่ง")
        print("ทั้งหมดราคา", 15 * amount, "บาท")
        print("--------------------------")
        print("      ขอบคุณที่ใช้บริการ")
        print("--------------------------")
    elif userSelected1 == 5:
        amount = int(input("ใส่จำนวนสินค้า"))
        print("----------Bill------------")
        print("ยางลบ", amount, "ชิ้น")
        print("ทั้งหมดราคา", 8 * amount, "บาท")
        print("--------------------------")
        print("      ขอบคุณที่ใช้บริการ")
        print("--------------------------")
    elif userSelected1 == 6:
        amount = int(input("ใส่จำนวนสินค้า"))
        print("----------Bill------------")
        print("ไม้บรรทัด", amount, "ด้าม")
        print("ทั้งหมดราคา", 15 * amount, "บาท")
        print("--------------------------")
        print("      ขอบคุณที่ใช้บริการ")
        print("--------------------------")
    elif userSelected1 == 7:
        amount = int(input("ใส่จำนวนสินค้า"))
        print("----------Bill------------")
        print("น้ำยาลบคำผิด", amount, "แท่ง")
        print("ทั้งหมดราคา", 25 * amount, "บาท")
        print("--------------------------")
        print("      ขอบคุณที่ใช้บริการ")
        print("--------------------------")
    elif userSelected1 == 0:
        print("ออกจากระบบ")
else:
    print("Error!!!")
