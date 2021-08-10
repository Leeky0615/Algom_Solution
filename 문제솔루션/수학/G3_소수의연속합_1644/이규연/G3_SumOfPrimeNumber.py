from math import sqrt

n = int(input())

arr = [False, False] + [True] * (n - 1)
pnArr = []
for i in range(2, int(sqrt(n)) + 1):
    if arr[i]:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1

for i, x in enumerate(arr):
    if x:
        pnArr.append(i)

start = 0
end = 0
count = 0
while start < len(pnArr) and end < len(pnArr):
    interval_sum = sum(pnArr[start:end + 1])
    if interval_sum >= n:
        start += 1
        if interval_sum == n:
            count += 1
    else:
        end += 1

print(count)
