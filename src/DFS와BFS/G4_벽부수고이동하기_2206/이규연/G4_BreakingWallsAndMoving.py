from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]  # 맵
visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]  # 벽의 상태까지 포함된 방문 배열

# 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0, 0, 0))  # (0,0)과 0(벽을 부순적 없음)을 큐에 넣음
    visit[0][0][0] = 1  # 시작점도 카운트
    while queue:
        x, y, status = queue.popleft()
        if x == n - 1 and y == m - 1:  # 큐에서 뽑은 좌표가 제일 끝 좌표인 경우
            return visit[x][y][status]  # 값 리턴
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:  # 인접한 값이 지도 안에 있을 경우
                if arr[nx][ny] == 1 and status == 0:  # 벽을 만났는데 벽을 부순적이 없는 경우
                    visit[nx][ny][status + 1] = visit[x][y][status] + 1  # 벽 부순 상태(1)의 값에 경로수를 추가
                    queue.append((nx, ny, status + 1))
                if arr[nx][ny] == 0 and visit[nx][ny][status] == 0:  # 벽이 없고, 방문한 적이 없는 경우
                    visit[nx][ny][status] = visit[x][y][status] + 1  # 경로 추가
                    queue.append((nx, ny, status))
    return -1  # 반복문을 통해 x,y의 좌표가 (n,m)에 도달하지 못한 경우 -1 리턴


print(bfs())
