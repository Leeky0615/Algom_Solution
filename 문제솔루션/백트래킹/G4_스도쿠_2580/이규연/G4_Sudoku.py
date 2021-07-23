g = []
blank = []
for i in range(9):
    temp = list(map(int, input().split()))
    for j in range(9):
        if temp[j] == 0:
            blank.append((i, j))
    g.append(temp)


def checkAvailableNum(i, j):
    check = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for k in range(9):
        if g[i][k] in check:  # 가로줄 확인
            check.remove(g[i][k])  # 해당 좌표의 값을 체크리스트에서 제거
        if g[k][j] in check:  # 세로줄 확인
            check.remove(g[k][j])  # 해당 좌표의 값을 체크리스트에서 제거
    i //= 3
    j //= 3
    for x in range(i * 3, (i + 1) * 3):
        for y in range(j * 3, (j + 1) * 3):
            if g[x][y] in check:
                check.remove(g[x][y])

    return check


status = False


def dfs(x):
    global status
    if status:
        return
    if x == len(blank):
        for r in g:
            print(*r)
        status = True
        return
    else:
        (i, j) = blank[x]
        availableNum = checkAvailableNum(i, j)

        for n in availableNum:
            g[i][j] = n
            dfs(x + 1)
            g[i][j] = 0

dfs(0)
