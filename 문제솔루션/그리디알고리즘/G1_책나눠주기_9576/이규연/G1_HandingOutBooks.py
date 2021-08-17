
# sys.stdin = open("input.txt", "r")

import sys
t = int(sys.stdin.readline())

for i in range(t):
    N, M = map(int, sys.stdin.readline().split())
    arr = []

    books = [False] * (N + 1)
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        arr.append((a, b))
    arr.sort(key=lambda x: x[1])

    result = 0
    while arr:
        a, b = arr.pop(0)
        for i in range(a, b + 1):
            if not books[i]:
                result += 1
                books[i] = True
                break
    print(result)
