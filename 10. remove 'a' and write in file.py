f = open("test.txt",'r') 
g = open("text2.txt",'w') 
str = " "
listoflines = f.readlines()
for list in listoflines:
    curlist = list.split()
    if "a" in curlist:
        print("a is present")
    else:
        g.write(list)

f.close() 
g.close()


