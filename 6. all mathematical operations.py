def calc(x,y):
    return x+y, x-y, x*y, x/y, x//y, x**y, x%y

num1 = int(input("Enter Your first number : "))
num2 = int(input("Enter Your second number : "))
sum, minus, mult, div, flodiv, power, mod = calc(num1,num2)
print("Sum of Your Numbers : ",sum)
print("Subtraction of Your Numbers : ",minus)
print("Multiplication of Your Numbers : ",mult)
print("Division of Your Numbers : ",div)
print("Floor Division of Your Numbers : ",flodiv)
print(num1, "Raise to Power ",num2," : ",power)
print("Remainder of Your Numbers : ",mod)