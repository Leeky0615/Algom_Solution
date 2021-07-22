# from collections import deque
#
g = [list(map(int, input().split())) for _ in range(9)]
verticals = [[0] * 9 for _ in range(9)]
box = [[0] * 9 for _ in range(9)]
for i in range(9):
    for j in range(9):
        box[i][j] = g[i//3][j//3]
        verticals[i][j] = g[j][i]


print(g)
print("-----------")
print(verticals)
# blank = deque()
# for i in range(9):
#     for j in range(9):
#         if g[i][j] == 0:
#             blank.append(i, j)
#
# while blank:
#     x, y = blank.popleft()
#     for i in range(9):
#         if g[x].count(i) != 1 and :

# 가로,세로, 3x3 체크 했을 때 빈칸이 하나면 바로 넣기..
