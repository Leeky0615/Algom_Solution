from itertools import combinations

INF = int(1e9)  # 최소값을 찾기 위한 초기값(무한대) 설정

n, m = map(int, input().split())  # 크기, 치킨집 개수
arr = [list(map(int, input().split())) for _ in range(n)]  # 집, 치킨집 정보가 있는 지도
home, chicken = [], []  # 집, 치킨집 배열

for r in range(n):  # row
    for c in range(n):  # column
        if arr[r][c] == 1:  # 지도의 원소값 = 1 -> 집
            home.append((r, c))
        elif arr[r][c] == 2:  # 지도의 원소값 = 2 -> 치킨집
            chicken.append((r, c))

result = INF  # 결과값 초기 무한대로 설정
for c in combinations(chicken, m):  # 전체 치킨집 개수에서 남겨야하는 치킨집 m개 뽑음->조합
    distance = 0
    for h in home:  # 모든 집 반복
        '''
            집 <-> 치킨집 거리가 제일 짧은것을 distance에 더해줘야함.
            이때, 치킨집의 좌표는 위의 조합을 통해 뽑힌 m개의 치킨집을
            모두 확인
        '''
        distance += min([abs(h[0] - i[0]) + abs(h[1] - i[1]) for i in c])
    result = min(result, distance)  # 결과값은 반복문(조합을 통한 모든 값)이 반복될 때마다 더 작은값으로 변경

print(result)
