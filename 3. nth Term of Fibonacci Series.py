def fib(n):
	if n<= 0:
		print("Negative Number")
	elif n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fib(n-1)+fib(n-2)

x = int(input("Enter Your Desired nth Term : "))
print(fib(x))
