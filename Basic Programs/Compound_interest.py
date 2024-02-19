# Python Program for compound interest
p = int(input("Principle Ammount= "))
r = float(input("Rate="))
t = int(input("Time= "))
a = p*(pow((1+r/100),t))
print("Compound Interst= ",a-p)