# n=3
# ***
# **
# *
def pattern(n):
    for i in range(n):
        print("*"*(n-i))
n=int(input("Enter the value of n="))
pattern(n)