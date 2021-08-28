intX = 45
strX = "Gayan"
char = 'S'

totalStr1 = strX + " has " + \
    str(intX) + " marks for Maths and he got " + char + " grade"

totalStr2 = "%s has %i marks for Maths and he got %c grade" % (
    strX, intX, char)

print(totalStr1)
print(totalStr2)
