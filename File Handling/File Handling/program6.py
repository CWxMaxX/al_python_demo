fo = open("File Handling\\File Handling\\file6.txt", "r")

while 1:
    line = fo.readline()
    if not line:
        break
    print(line)
    # lineList = line.split(",")
    # # print(lineList)
    # # print(float(lineList[3]))
    # avg = (float(lineList[1])+float(lineList[2])+float(lineList[3]))/3
    # print(str(lineList[0]) + " Avarage = " + str(round(avg, 2)))

print("File read finished")
fo.close()
