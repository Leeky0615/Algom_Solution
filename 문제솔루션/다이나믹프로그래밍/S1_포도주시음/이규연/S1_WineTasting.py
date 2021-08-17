import sys

sys.stdin = open("input.txt", "rt")

n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

dp = [0]

for i in range(1, n + 1):
    if i == 1:
        dp.append(arr[1])
    elif i == 2:
        dp.append(arr[1]+arr[2])
    else:
        dp.append(max(dp[i - 1], (arr[i] + max(arr[i - 1] + dp[i - 3], dp[i - 2]))))

print(dp[n])
