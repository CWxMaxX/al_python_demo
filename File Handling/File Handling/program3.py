fo = open("File Handling\\File Handling\\file3.txt", "a+")
fo.write("File written completed\n")
fo.close()


fo = open("File Handling\\File Handling\\file3.txt", "r+")
s = fo.read()
print(s)
fo.close()
