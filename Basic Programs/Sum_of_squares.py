# Python Program for Sum of squares of first n natural numbers
n = int(input("Enter the value of n: "))
sum = 0
for i in range(1,n+1):
    sum = sum+ pow(i,2)
print(f"Sum of Squares of first {n}'th natural number= {sum}" )