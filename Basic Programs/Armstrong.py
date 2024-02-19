# Python Program to check Armstrong Number
n = int(input("Enter a no.= "))
x = n
y = n
i = 0
while x!=0:
    r = x%10
    i += 1
    x //=10
s = 0
while y!=0:
    t = y%10
    s = s+pow(t,i)
    # s += t ** i
    y //=10

if s == n:
    print(n," is a Armstrong number")
else:
    print(n," is not a Armstrong number")

# //	Floor division - division that results into whole number adjusted to the left in the number line	x // y
