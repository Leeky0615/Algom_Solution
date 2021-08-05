k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

start = 1
end = max(arr)
while start <= end:
    mid = (start + end) // 2
    total = 0
    for x in arr:
        total += x // mid

    if total >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
