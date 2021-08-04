from math import sqrt

min, max = map(int, input().split())

arr = [True] * (max - min + 1)
cnt = 0
for i in range(2, int(sqrt(max)) + 1):
    sqNum = i ** 2
    j = min // sqNum
    while sqNum * j <= max:
        idx = sqNum * j - min
        if idx >= 0 and arr[idx]:
            cnt += 1
            arr[idx] = False
        j += 1

print(len(arr) - cnt)
