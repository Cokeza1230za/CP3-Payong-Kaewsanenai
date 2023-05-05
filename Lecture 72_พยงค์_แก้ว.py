menuList = []

def showBill():
    print('Cokeza007'.center(34, '-'))
    total = 0
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1], 'บาท')
        total += int(menuList[number][1])
    print("ราคารวมทั้งหมด:", total, "บาท")
    print('ขอบคุณที่ใช้บริการนะครับ'.center(40, '-'))


while True:
    menuName = input("ใส่เมนูมาไอน้อง >>")
    if (menuName.lower() == "exit"):
        print("ออกเลยไอน้อง")
        break
    else:
        menuPrice = input("ใส่ราคามาไอน้อง >>")
        menuList.append([menuName,menuPrice])


print(menuList)
showBill()
