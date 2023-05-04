menuList = []
priceList = []

def showBill():
    total = 0
    print("-----Cokeza 007 Food-----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
        total += int(priceList[number])
    print("ราคารวมทั้งหมด :",total)


while True:
    menuName = input("ใส่เมนู")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("ใส่ราคาเมนู")
        menuList.append(menuName)
        priceList.append(menuPrice)
print(menuList, priceList)
showBill()
