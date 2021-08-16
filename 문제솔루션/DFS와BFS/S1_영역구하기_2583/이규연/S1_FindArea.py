# import sys
#
# sys.stdin = open("input.txt", "rt")

from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    arr[y][x] = -1
    size = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and arr[ny][nx] == 0:
                arr[ny][nx] = -1
                size += 1
                q.append((nx, ny))
    return size


M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]
result = []
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1

for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            result.append(bfs(j, i))
print(len(result))
print(*sorted(result))
