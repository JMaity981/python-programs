# Python Program for factorial of a number
n= int(input("Enter a Number: "))
f=1
for x in range(1,n+1):
    f=f*x
print(f"Factorial of {n}= {f}")