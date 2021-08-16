import sys

sys.stdin = open("input.txt", "r")

from math import sqrt

def goldbach(x):
    for p in range(3, x // 2 + 1):
        if isPrime[p] and isPrime[x - p]:
            return p, x - p
    else:
        return "Goldbach's conjecture is wrong."


isPrime = [False, False] + [True] * 1000000
for i in range(2, int(sqrt(1000000)) + 1):
    if isPrime[i]:
        j = 2
        while i * j <= 1000000:
            isPrime[i * j] = False
            j += 1

while True:
    n = int(input())
    if n == 0:
        break
    x, y = goldbach(n)
    print(n, '=', x, '+', y)
