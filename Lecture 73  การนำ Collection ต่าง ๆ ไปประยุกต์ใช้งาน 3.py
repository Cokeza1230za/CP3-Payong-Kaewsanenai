systemMenu = {"ไก่ย่างวิเชียรบุรี": 35, "ไก่ทอดหาดใหญ่": 45, "กะเพราหมูกรอบ": 55, "ผักทอด": 20}
menuList = []


def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])


while True:
    menuName = input("Plese Enter Menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])

showBill()
