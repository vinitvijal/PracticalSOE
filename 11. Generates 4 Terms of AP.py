def AP(a,d):
    a2 = a + d
    a3 = a + 2*d
    a4 = a + 3*d
    a5 = a + 4*d
    print("")
    print("Terms Of AP : ",a, a2, a3, a4, a5)


a = int(input("Enter Initial Number of AP : "))
d = int(input("Enter Common Difference of AP : "))

AP(a,d)