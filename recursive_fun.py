# n=5
# 1+2+3+4+5
def sum(n):
    if n==0 or n==1:
        return n
    else:
        return n+sum(n-1)
n=5
print(f"sum of first {n} natural numbers= {sum(n)}")