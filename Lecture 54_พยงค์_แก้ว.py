def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        print("Done!")
        return showMenu()
    else:
        print("Invalid username or password!")
        return login()


def showMenu():
    print("----- Cokeza007 -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

    userSelected = int(input(">>"))
    if userSelected == 1:
        return vatCalculator()
    elif userSelected == 2:
        return priceCalculator()


def vatCalculator(totalPrie):
    result = totalPrie +(totalPrie *7/100)
    return result


def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    result = price1 + price2
    return result

print(login())
