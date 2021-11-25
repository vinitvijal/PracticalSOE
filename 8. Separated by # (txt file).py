file = open("test.txt",'r') 
listoflines = file.readlines()
for i in listoflines:
    line = i.split(" ")
    for j in range(len(line)-1):
        print(line[j], end="#")
    print()

file.close()