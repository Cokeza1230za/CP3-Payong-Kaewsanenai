menuList = []
priceList = []


def showBill():
    print('Cokeza007'.center(25, '-'))
    total = 0
    for number in range(len(menuList)):
        print(menuList[number], 'บาท', priceList[number], 'บาท')
        total += int(priceList[number])
    print("ราคารวมทั้งหมด:", total, "บาท")


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
