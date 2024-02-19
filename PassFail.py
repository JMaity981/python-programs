m1 = float(input("Enter the marks 1: "))
m2 = float(input("Enter the marks 2: "))
m3 = float(input("Enter the marks 3: "))
if (m1<33 or m2<33 or m3<33 or (m1+m2+m3)/3<40):
    print("You Failed the exam")
else:
    print("You passed the exam")