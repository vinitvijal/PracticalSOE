file = open("test.txt",'r') 
line = " "
vowels = 0
conso = 0
upper = 0
lower = 0 
while line:
    line = file.read(1)
    if line in ['a','A','e','E','i','I','o','O','u','U']:
        vowels+=1
    if line.isupper():
        upper+=1
    elif line.islower():
        lower+= 1
    elif line.isupper():
        upper+=1
        conso+=1
    elif line.islower():
        lower+= 1
        conso+=1
print("Number of Vowels : ",vowels)
print("Number of Consonants : ",conso)
print("Number of Uppercase Letters : ",upper)
print("Number of Lowercase Letters : ",lower)