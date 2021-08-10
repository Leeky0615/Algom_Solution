from math import factorial

n = int(input())
fac = factorial(n)

count = 0
for i in str(factorial(n))[::-1]:
    if int(i) != 0:
        print(count)
        break
    else:
        count += 1
