str1 = "saman takes the 1st place"

str1_m1 = str1.capitalize()
str1_m12 = str1.title()

print(str1_m1)  # Capitalize only first character
print(str1_m12)  # Capitalize every first character of words
print("\n")


str2 = "Samsung"

x = str2.count("s", 0, 2)  # case sensitive
y = str2.find("s")  # return index of substring
z = str2.index("s")

print("X", x)
print("Y", y)
print("Z", z)

print("\n")

str3 = "Cricket"

m5 = str3.upper()
m6 = str3.lower()

print(m5)
print(m6)
print("\n")

str4 = "SamsungZx"

m8 = max(str4)
m9 = min(str4)
print(m8)
print(m9)
print("\n")

str5 = "*****This is string example....wow!!!*****"


m10 = str5.strip("i")
print(m10)
print("\n")


str6 = "CS:320880:GM:0053"

m11 = str6.split(":")

print(m11)
print(m11[1])
print("\n")

str7 = "Sam123"
str8 = "#$%!"
str9 = "saman"
str10 = "123456"

m15 = str7.isalpha()
m15_2 = str9.isalpha()

print(m15)
print(m15_2)

m16 = str7.isalnum()
m16_2 = str9.isalnum()
m16_3 = str8.isalnum()

print(m16)
print(m16_2)
print(m16_3)

m17 = str10.isdigit()
m17_2 = str7.isdigit()
m18 = str10.isnumeric()

print(m17)
print(m17_2)
print(m18)

str11 = "*".join(str9)
print(str11)

print(str4.swapcase())
