def wordinsentence(a, b):
    s = a.split(" ")
 
    for i in s:
        if (i == b):
            return True
    return False
 

s = input("Enter Your Sentence : ")
word = input("Enter Your Word(to be checked) : ")
 
if (wordinsentence(s, word)):
    print(word ,"is Present in Your Sentence!!!")
else:
    print("No, Your Word is Not Present in Your Sentence.")
 