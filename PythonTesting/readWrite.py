#Read all the content of the file
#read n number of characters by passing parameter
#print(file.read(5))
#read one single line at a time readLine()
file = open("ttest.txt")

#print(file.read(3))

#read one single line at a time readline
#print(file.readline())
#print(file.readline())


#print line by line using readline method
#line = file.readline()
#while line != "":
#    print(line)
#    line = file.readline()#


for i in file.readlines():
    print(i)
#print(file.readline())
#print(file.readline())

#file.readline()

file.close()