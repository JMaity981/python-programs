#Python Program to find sum of array
arr = [] 
# number of elemetns as input
 
n = int(input("Enter number of elements : "))  
# iterating till the range 

for i in range(0, n): 
    ele = int(input()) 
    arr.append(ele) # adding the element 

# initialize a variable 
# to store the sum 
# while iterating through 
# the array later 
sum=0
     
# iterate through the array 
# and add each element to the sum variable 
# one at a time 
for i in arr: 
    sum = sum + i  
  
# display sum  
print ('Sum of the array is= ', sum)  
  
# This code is contributed by Himanshu Ranjan  