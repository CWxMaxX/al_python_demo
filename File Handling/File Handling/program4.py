f = open("File Handling\\File Handling\\file5.txt", "w")
i = 1
while i <= 10:
    f.write("%i\n" % i)
    i += 1
f.close

f = open("File Handling\\File Handling\\file5.txt", "r")
s = f.read()
print(s)
f.close()
