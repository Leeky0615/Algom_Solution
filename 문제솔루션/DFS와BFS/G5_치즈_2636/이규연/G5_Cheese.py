import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():
    visited = [[False] * w for _ in range(h)]
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = True
    cnt = 0
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx]:
                if arr[ny][nx] == 0:
                    visited[ny][nx] = True
                    queue.append([ny, nx])
                if arr[ny][nx] == 1:
                    arr[ny][nx] = 0
                    cnt += 1
                    visited[ny][nx] = True
    counts.append(cnt)
    return cnt


h, w = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]
counts = []

time = 0
while True:
    time += 1
    count = bfs()
    if count == 0:
        break

print(time - 1)
print(counts[-2])
