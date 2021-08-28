# Open a file
# fo = open("D:\\AL_ICT\\Pending\\PythonTestPrograms\\File Handling\\File Handling\\test.txt", "w")
fo = open("test.txt", "w")
print("Name of the file: ", fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
fo.close()
