def solution(n, build_frame):
    global board, board_size
    board = [[[-1,-1] for _ in range(n + 1)] for _ in range(n + 1)]
    board_size = n
    answer = []
    for build in build_frame:
        x, y = build[0], build[1]
        structure, operation = build[2], build[3]
        possibility = False
        if operation == 1:
            board[y][x][structure] = structure
            if structure == 0:
                if isPossibleColumn(x, y):
                    possibility = True
            else:
                if isPossibleRow(x, y):
                    possibility = True
            if not possibility:
                board[y][x][structure] = -1
        else:
            board[y][x][structure] = -1
            if structure == 0:
                if isPossibleRow(x - 1, y + 1) and isPossibleRow(x, y + 1) and isPossibleColumn(x, y + 1):
                    possibility = True
            else:
                if isPossibleRow(x - 1, y) and isPossibleRow(x + 1, y) and isPossibleColumn(x,y) and isPossibleColumn(x+1,y):
                    possibility = True
            if not possibility:
                board[y][x][structure] = structure
    for y in range(n + 1):
        for x in range(n + 1):
            for structure in range(2):
                if board[y][x][structure] != -1:
                    answer.append([x, y, structure])
    return sorted(answer)


def isRow(x, y):
    global n
    if x < 0 or x > board_size or y < 0 or y > board_size:
        return False
    else:
        return True if board[y][x][1] == 1 else False


def isColumn(x, y):
    global n
    if x < 0 or x > board_size or y < 0 or y > board_size:
        return False
    else:
        return True if board[y][x][0] == 0 else False


def isPossibleRow(x, y):
    if isColumn(x, y - 1) or isColumn(x + 1, y - 1):
        return True
    if isRow(x - 1, y) and isRow(x + 1, y):
        return True
    return False


def isPossibleColumn(x, y):
    if y == 0:
        return True
    if isColumn(x, y - 1):
        return True
    if isRow(x - 1, y) or isRow(x, y):
        return True
    return False


build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
               [3, 2, 1, 1]]
n = 5
print(sorted(solution(n, build_frame)))
