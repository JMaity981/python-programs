# Python program to print all Prime numbers in an Interval
start = int(input("Enter The Start Value: "))
end = int(input("Enter the End Value: "))
for i in range(start, end+1): 
  if i>1: 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else:
        print(i) 