from collections import deque

INF = 1e9  # 무한대 -> 10억으로 초기화

n = int(input())  # 지도 크기 입력

graph = []
bs_size = 2  # 상어 크기
bs_x, bs_y = 0, 0  # 상어 위치 초기화

for i in range(n):
    # 물고기, 상어의 위치를 입력 받음
    temp = list(map(int, input().split()))
    for j in range(n):
        # 만약 입력받은 값이 9라면
        if temp[j] == 9:
            # 상어의 위치좌표 저장
            bs_x, bs_y = i, j
    graph.append(temp)

graph[bs_x][bs_y] = 0  # 상어 위치 0으로 변경

# 방향벡터
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# 이동가능한 위치에 대해서 거리 갱신
def bfs():
    # 거리를 나타낼 리스트 초기화
    visited = [[-1] * n for _ in range(n)]
    # 초기 상어 위치 큐에 담기
    queue = deque([(bs_x, bs_y)])
    # 상어의 시작위치는 0으로 갱신
    visited[bs_x][bs_y] = 0
    # 큐의 값이 없어질 떄까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 지도에서 벗어나지 않고
            if 0 <= nx < n and 0 <= ny < n:
                # 물고기의 값이 상어의 크기보다 같거나 작을때만 이동
                if visited[nx][ny] == -1 and graph[nx][ny] <= bs_size:
                    # 현재 상어위치 + 1 의 값을 거리리스트에 저장
                    visited[nx][ny] = visited[x][y] + 1
                    # 다음 위치를 큐에 저장
                    queue.append((nx, ny))
    # 최종적으로 갱신된 거리리스트 리턴
    return visited


# 먹을 수 있는 물고기를 찾는 함수
def possibleToEat(visited):
    sec = INF  # 소요되는 시간을 무한으로 초기화

    # 입력 받은 거리리스트 원소 하나씩 탐색
    for i in range(n):
        for j in range(n):
            # 상어가 움직일 수 있는 위치이고 (-1이 아님) 상어가 먹을 수 있는 물고기위치
            if visited[i][j] != -1 and 1 <= graph[i][j] < bs_size:
                # 해당 위치의 소요시간이 이전에 탐색한 소요시간 보다 작을 경우
                if visited[i][j] < sec:
                    sec = visited[i][j]  # 소요시간 갱신 (작은 값으로)
                    x, y = i, j  # 해당 위치도 갱신
    # 한번도 갱신이 안됐을 경우
    if sec == INF:
        return None
    # 갱신이 된 경우
    else:
        # 좌표, 소요시간 리턴
        return x, y, sec


result = 0  # 최종 결과값
sizeUpCount = 0  # 상어가 먹은 물고기 수
while True:
    value = possibleToEat(bfs())
    # 결과값이 없는 경우 (먹을 수 있는 물고기 없음)
    if value == None:
        # 최종 소요시간 출력
        print(result)
        break
    # 아닐 경우
    else:
        # 현재 좌표, 소요시간 갱신
        bs_x, bs_y = value[0], value[1]
        result += value[2]

        graph[bs_x][bs_y] = 0  # 현재 좌표(먹은 위치) 갱신
        sizeUpCount += 1  # 먹은 물고기 수 추가

        # 먹은 물고기 수가 상어의 사이즈보다 크거나 같을 경우
        if sizeUpCount >= bs_size:
            bs_size += 1  # 상어 크기를 키움
            sizeUpCount = 0  # 먹은 물고기 수 초기화
