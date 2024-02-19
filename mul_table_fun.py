def mul_table(n):
    mul=0
    for i in range(10):
        mul=mul+n
        print(f"{n}*{i+1}={mul}")
mul_table(5)