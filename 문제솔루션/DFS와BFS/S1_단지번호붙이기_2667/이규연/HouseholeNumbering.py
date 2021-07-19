n = int(input())  # 지도크기 입력 받기

# 지도 정보 입력 받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 방향 벡터 초기화
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# dfs 함수 선언
def dfs(x, y):
    graph[x][y] = 0  # 해당 가구 방문 처리
    global cnt  # 전역 변수 선언
    cnt += 1  # 가구수 추가
    # 방향벡터(4방향)에 대해서 모두 확인
    for i in range(4):
        # 확인할 새로운 좌표
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:  # 지도 범위를 벗어나지 않을 때만
            if graph[nx][ny] == 1:  # 해당 좌표에 방문하지 않은 집이 있는 경우
                dfs(nx, ny)  # 새로운 좌표에 대해 dfs 수행


apartment = []  # 단지 수를 표시할 리스트 선언
# 모든 지도를 탐색
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:  # 해당 좌표에 방문하지 않은 집이 있는 경우
            cnt = 0  # 가구수 초기화
            dfs(i, j)  # 해당 좌표에 대해서 dfs 수행
            apartment.append(cnt)  # 단지의 가구수 추가

print(len(apartment))  # 단지 개수 출력

# 저장된 단지에 있는 가구수를 오름차순으로 출력
for cnt in sorted(apartment):
    print(cnt)
