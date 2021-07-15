def bfs(x):
    queue = deque([x])
    bipartiteState[x] = 1
    while queue:
        value = queue.popleft()
        for i in graph[value]:
            if bipartiteState[i] == 0:
                bipartiteState[i] = -1 * bipartiteState[value]
                queue.append(i)
            elif bipartiteState[i] == bipartiteState[value]:
                return False
    return True


from collections import deque

t = int(input())  # 테스트케이스 개수
for _ in range(t):
    v, e = map(int, input().split())  # 정점(V) , 간선(e)
    graph = [[] for _ in range(v + 1)]  # 정점+1 만큼 만듬 -> 첫번째 값 사용X
    bipartiteState = [0] * (v + 1)  # 이분상태 배열 -> graph와 마찬가지로 첫번째 값 사용X
    flag = False  # 이분그래프 가능 결과 Flag

    for _ in range(e):  # 간선 수 만큼 반복해서 graph 채우기
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, v + 1):  # 첫번째 인덱스 사용X -> 1~V 까지만 사용
        if bipartiteState[i] == 0:  # 만약 이분그래프 상태 배열 값이 0이라면 -> 아직 BFS 수행이 안되었다면
            flag = bfs(i)  # bfs 수행
            if not flag:  # flag가 Flase라면 중지
                break

    print("YES" if flag else "NO")
