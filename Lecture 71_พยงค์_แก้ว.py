menuList = []
priceList = []


def showBill():
    print('Cokeza007'.center(34, '-'))
    total = 0
    for number in range(len(menuList)):
        print(menuList[number], priceList[number], 'บาท')
        total += int(priceList[number])
    print("ราคารวมทั้งหมด:", total, "บาท")
    print('ขอบคุณที่ใช้บริการนะครับ'.center(40, '-'))


while True:
    menuName = input("ใส่เมนูมาไอน้อง >>")
    if (menuName.lower() == "exit"):
        print("ออกเลยไอน้อง")
        break
    else:
        menuPrice = input("ใส่ราคามาไอน้อง >>")
        menuList.append(menuName)
        priceList.append(menuPrice)

print(menuList, priceList)
showBill()
