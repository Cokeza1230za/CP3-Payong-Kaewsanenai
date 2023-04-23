inputNumbers = int(input("กรอกตัวเลข : "))
for i in range(inputNumbers):
    print((" " * (inputNumbers - i - 1)) + ("*" + ("*" * (i * 2))))

