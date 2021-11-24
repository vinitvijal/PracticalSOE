def sumoflist(list):
    sum = 0
    for i in list:
        sum += i
    return sum

list = list(eval(input("Enter Your List : ")))
sum = sumoflist(list)
print("Sum of Your Numbers is ",sum)
