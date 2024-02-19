#Python Program for cube sum of first n natural numbers
n = int(input("Enter the value of n: "))
sum = 0
for i in range(1,n+1):
    sum = sum+ pow(i,3)
print(f"Cube Sum of first {n}'th natural numbers= {sum}" )