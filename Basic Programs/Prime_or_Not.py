# Python program to check whether a number is Prime or not
n = int(input("Enter A Number= "))
for x in range (2,n):
    if(n%x==0):
        print(n," is a Prime Number")
        break
else:
    print(n," is a Not Prime Number")