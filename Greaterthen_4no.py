print("Enter the 4 no.")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if(a>b):
    max1 = a
else:
    max1 = b
if(c>d):
    max2 = c
else:
    max2 = d
if(max1>max2):
    print("Greatest number = ", max1)
else:
    print("Greatest number = ", max2)