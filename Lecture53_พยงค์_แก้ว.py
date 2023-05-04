def VatCalculator(TotalPrice):
    result = TotalPrice + (TotalPrice * 7 / 100)
    return result


inputData = int(input("ใส่ราคามาไอน้อง THB :"))
print(VatCalculator(inputData))
