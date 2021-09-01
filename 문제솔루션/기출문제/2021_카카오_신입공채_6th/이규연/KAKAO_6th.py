import copy
import math
from collections import deque
from itertools import permutations

size = 4


def check_cards_point(board):
    temp = {}
    for r in range(size):
        for c in range(size):
            key = board[r][c]
            if key != 0:
                if key in temp.keys():
                    temp[key].append((r, c))
                else:
                    temp[key] = [(r, c)]
    return temp


def dist(p1, p2, board, cursor):
    cToP = 0


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]




# def bfs(p1, p2, board):
#     visited = [[False] * size for _ in range(size)]
#     q = deque()
#     q.append(p1)
# while q:
#     y, x = q.popleft()
#     visited[y][x] = True
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if min(p1[0], p2[0]) <= ny <= max(p1[0], p2[0]) and min(p1[0], p2[0]) <= ny <= max(p1[0], p2[0]) and not visited[ny][nx]:
#             if (ny,nx) == p2:
#                 break
#             else:
#                 if board[ny][nx] == 0:
#                     q.append((ny,nx))


def calc(board, cards, pList, cursor):
    if not pList:
        return 0
    b = copy.deepcopy(board)
    l = copy.deepcopy(pList)
    currV = l.pop()
    p1, p2 = cards[currV]
    distOp1 = dist(p1, p2, b, cursor)
    distOp2 = dist(p2, p1, b, cursor)
    b[p1[0]][p1[1]] = 0
    b[p2[0]][p2[1]] = 0
    return min(distOp1 + calc(b, l, p2), distOp2 + calc(b, l, p1))


def solution(board, r, c):
    cards = check_cards_point(board)
    answer = math.inf
    for per in permutations(cards.keys()):
        min_dist = min(min_dist, calc(board, cards, list(per), (r, c)))
    return answer


dx = [1, 0, -1, 1]
dy = [0, 1, 0, -1]
boards = [[[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]],
          [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]]]
rs = [1, 0]
cs = [0, 1]
result = [14, 16]
for i in range(2):
    print('-------- SOLUTION', i, '--------')
    cards = check_cards_point(boards[0])
    print('1. cards :', cards)
    pList = permutate(cards)
    print('2. permutatation :', pList)
    # solution(board[i], r[i], c[i])
    print('-------- RESULT', result[i], '--------\n')
