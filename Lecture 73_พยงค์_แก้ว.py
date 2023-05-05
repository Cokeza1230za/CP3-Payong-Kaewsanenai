systemMenu = {"กาแฟดำ": 25, "ชานมเย็น": 25, "นมสดเย็น": 25, "โกโก้เย็น": 25, "โอวัลตินเย็น": 25, "ชาเขียวนม": 25}
menuList = []


def showBill():
    print('Coke007 Drinks'.center(32, '-'))
    total = 0
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1], 'บาท')
        total += int(menuList[number][1])
    print("ราคารวมทั้งหมด:", total, "บาท")
    print('ขอบคุณที่ใช้บริการนะครับ'.center(40, '-'))


while True:
    menuName = input("ใส่เมนูมาไอน้อง >>")
    if (menuName.lower() == "exit"):
        print("ออกเลยไอน้อง!!!")
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])

print(menuList)
showBill()
