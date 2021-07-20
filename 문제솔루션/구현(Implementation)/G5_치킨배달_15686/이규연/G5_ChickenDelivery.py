from itertools import combinations
INF = int(1e9)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
home, chicken, dist = [], [], [[] for _ in range(m)]

for r in range(n):
    for c in range(n):
        if arr[r][c] == 1:
            home.append((r, c))
        elif arr[r][c] == 2:
            chicken.append((r, c))

for i in range(m):
    for h in home:
        length = abs(chicken[i][0] - h[0]) + abs(chicken[i][1] - h[1])
        dist[i].append(length)

print(dist)

# result = INF
# for c in combinations(dist, m):
#     print(c)
#     minDist = 0
#     for i in range(len(home)):
#         minDist += min(c[i])
#     result = min(result, minDist)
#
# print(result)
