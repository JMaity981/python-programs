n = int(input("Enter the value of n= "))
for i in range(n):
    if (i==0 or i==n-1):
        print("* "*(n),end="")
    else:
        print("*",end="")
        print("  "*(n-2),end="")
        print(" *",end="")
    print("\n",end="")

# Enter the value of n= 3
# * * *
# *   *
# * * *
