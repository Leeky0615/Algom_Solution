n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
start = 0
end = max(arr)
while start <= end:
    mid = (start + end) // 2
    total = 0
    for x in arr:
        if x > mid:
            total += x - mid

    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
