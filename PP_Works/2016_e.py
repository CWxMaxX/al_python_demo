itemQtyList = []
j = 0
while j < 10:
    qty = int(input("Quntity of item " + str(j+1) + " = "))
    itemQtyList.append(qty)
    j += 1
print(itemQtyList)

itemPriceList = [10, 12, 15, 10, 25, 45, 50, 25, 10, 12]
i = 0
total = 0
while i < 10:
    total = total + (itemQtyList[i]*itemPriceList[i])
    i += 1

print("Total = ", total)
