import sys, heapq

# sys.stdin = open("input.txt", "rt")

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(arr, (abs(x), x))
    else:
        try:
            print(heapq.heappop(arr)[1])
        except:
            print(0)
