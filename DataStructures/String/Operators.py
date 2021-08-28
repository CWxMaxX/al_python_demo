str1 = "Hello"
str2 = "Python"
str3 = "*"


op1 = str1 + str2
op2 = str3*20
op3 = str2[2]
op4 = str2[2:4]

print(op1)
print(op2)
print(op3)
print(op4)

#############################################

str4 = "BMT2031"
str5 = "BMT21320"


def sep(strX):
    print("Year = 20" + strX[3:5])
    print("Person = ", strX[5:])


sep(str4)
sep(str5)

#############################################

str6 = "Samsung"

valIn = "u" in str6
valIn2 = "d" in str6
valIn3 = "u" not in str6
valIn4 = "d" not in str6

print(valIn)
print(valIn2)
print(valIn3)
print(valIn4)

ex2 = "CS320880GM0053"
ex2_2 = "ON325145CL1002"


def sep2(strX):
    docType = strX[:2]
    indexNum = strX[2:8]
    dist = strX[8:10]
    count = strX[10:]

    if docType == "CS":
        docType = "Character Certificate"
    elif docType == "ON":
        docType = "Official Notice"

    if dist == "GM":
        dist = "Gampaha"
    if dist == "CL":
        dist = "Colombo"

    print(docType)
    print(indexNum)
    print(dist)
    print(count)


sep2(ex2)
sep2(ex2_2)
