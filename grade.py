marks = int(input("Enter the marks= "))
if(marks<=100):
    print("Grade:",end=" ")
    if(marks>=90):
        print("Ex")
    elif(marks>=80):
        print("A")
    elif(marks>=70):
        print("B")
    elif(marks>=60):
        print("C")
    elif(marks>=50):
        print("D")
    else:
        print("F")
else:
    print("are you entered greater then of 100")
