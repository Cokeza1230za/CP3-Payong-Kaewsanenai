def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        return login()

def showMenu():
    print("------Done!!!------")
    print("---Cokeza007 Shop ---")
    print("1. คำนวณราคาสินค้าพร้อมกับภาษี")
    return menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        return priceCalculator()
    else:
        return login()
def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("ใส่ราคาสินค้าชิ้นแรก : "))
    price2 = int(input("ใส่ราคาสินค้าชิ้นที่ 2 : "))
    return vatCalculator(price1 + price2)


print(login())