from collections import deque

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def find_tomato(box):
    queue = deque()
    for i in range(len(box)):
        for j in range(len(box[i])):
            if box[i][j] == 1:
                queue.append((i, j))
    if queue:
        return queue
    else:
        return -1


def change_tomato(box, queue):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))


def count_0(box):
    count = False
    for i in box:
        if i.count(0) != 0:
            count = True
    return count


if not count_0(box):
    print(0)
else:
    queue = find_tomato(box)
    if queue == -1:
        print(-1)
    else:
        change_tomato(box, queue)
        if not count_0(box):
            result = 0
            for i in box:
                result = max(result, max(i))
            print(result - 1)
        else:
            print(-1)
