import sys

sys.stdin = open("input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))

result = [arr[0]]
for i in range(n - 1):
    result.append(max(result[i] + arr[i + 1], arr[i + 1]))

print(max(result))
