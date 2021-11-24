#To be completed

f = open("test.txt",'r') 
g = open("text2.txt",'w') 
str = " "
listoflines = f.readlines()
for line in listoflines:
    words = line.split()
    for i in words:
        letter = i.split()[0]



# while str:
#     str = f.readline() 
#     if 'a' in str:
#         g.write(str)
# f.close() 
# g.close()


