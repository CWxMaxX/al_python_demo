homeId = input("ID")
postR = input("Post Reading")
preR = input("Present Reading")

usedUnits = int(preR) - int(postR)

if usedUnits > 64:
    payment = (usedUnits-64)*10 + (64*5)

else:
    payment = usedUnits * 5

print(payment)
