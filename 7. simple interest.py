def simp(prin, time=2, rate=0.10):
    return prin * time * rate

prin = float(input("Enter Your Principal Amount : "))
time = float(input("Enter Your Time Period(in yrs) : "))
rate = float(input("Enter Your Rate of Interest : "))
newRate = rate/100
si = simp(prin, time, newRate)
print("Your Simple Interest : ",si)