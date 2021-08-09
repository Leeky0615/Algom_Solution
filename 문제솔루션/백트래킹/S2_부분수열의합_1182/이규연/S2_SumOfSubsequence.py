import sys

sys.stdin = open("input.txt", "rt")

n, s = map(int, input().split())
arr = list(map(int, input().split()))
count = 0


def dfs(index, sum):
    global count
    if index >= n:
        return
    sum += arr[index]
    if sum == s:
        count += 1
    dfs(index + 1, sum - arr[index])
    dfs(index + 1, sum)


dfs(0, 0)
print(count)
