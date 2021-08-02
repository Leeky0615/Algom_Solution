n = int(input())
arr = list(map(int, input().split()))

arr.sort()
comp = 0
for i in arr:
    if i == comp:
        continue
    else:
        print(i, end=' ')
        comp = i
