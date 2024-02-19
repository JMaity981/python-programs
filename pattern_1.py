n = int(input("Enter the value of n= "))
x=1
y=n-1
for i in range(n):
    for j in range(y):
        print(" ",end="")
    y=y-1
    for k in range(x):
        print("*",end="")
    x=x+2
    print("\n",end="")

# Enter the value of n= 3
#   *
#  ***
# *****