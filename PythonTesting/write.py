#file = open("ttex.txt")

#file.close()
#We will read the file and store all the files in list an reverse the list;
# write the list back to file

#abc
#bcd
#ccc
#dddd
#xyz

with open("ttest.txt", "r") as reader:
    content = reader.readlines()
    reversed(content)
    with open("ttest.txt", "w") as writer:
        for i in reversed(content):
            writer.write(i)

