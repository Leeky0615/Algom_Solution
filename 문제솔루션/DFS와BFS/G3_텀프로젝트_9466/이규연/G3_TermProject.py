import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "rt")

t = int(input())


def dfs(currentNode):
    global result
    visited[currentNode] = True
    team.append(currentNode)
    nextNode = arr[currentNode]
    if visited[nextNode]:
        if nextNode in team:
            result -= len(team[team.index(nextNode):])
        return
    else:
        dfs(nextNode)


for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [True] + [False] * n
    result = n
    for i in range(1, n + 1):
        if not visited[i]:
            team = []
            dfs(i)
    print(result)
