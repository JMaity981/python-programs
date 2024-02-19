n = int(input("Enter the number: "))
cnd = 0
for i in range(2,n):
    if (n%i==0):
        print(n,"is a not prime number")
        cnd = 1
        break
if(cnd==0):
    print(n,"is a prime number")