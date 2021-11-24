file = open("test.txt",'r') 
str = ""
while str:
    str = file.readline().split()
    length = len(str)
    for i in range(length):
        print(str[i],end = "#")
        