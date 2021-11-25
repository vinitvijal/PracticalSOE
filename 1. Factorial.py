def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
    return f

x = int(input("Enter Your Number : "))
if x < 0:
    print("You Have Entered Negative Value!!!")
else:
    result = fact(x)
    print(result)


