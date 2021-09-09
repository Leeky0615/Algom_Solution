def solution(n, build_frame):
    global board

    answer = []
    for build in build_frame:
        x, y = build[0], build[1]
        structure, operation = build[2], build[3]
        print('좌표 : ', (x, y))
        if operation == 1:  # 설치
            board[y][x][structure] = structure
            print(' 설치 작업 시작 (', end='')
            possibility = False
            if structure == 0:
                print('기둥): ', end='')
                if isPossibleColumn(x, y):  # 기둥
                    possibility = True
            else:
                print('보): ', end='')
                if isPossibleRow(x, y):  # 보
                    possibility = True
            if not possibility:
                print('설치 불가능')
                board[y][x][structure] = -1
            else:
                print('설치 가능')
        else:  # 제거
            board[y][x][structure] = -1
            print(' 제거 작업 시작 (', end='')
            possibility = False
            if structure == 0:  # 기둥
                print('기둥): ', end='')
                if isPossibleRow(x - 1, y + 1) and isPossibleRow(x, y + 1) and isPossibleColumn(x, y + 1):
                    possibility = True
            else:  # 보
                print('보): ', end='')
                if isPossibleRow(x - 1, y) and isPossibleRow(x + 1, y) and isPossibleColumn(x,y) and isPossibleColumn(x+1,y):
                    possibility = True
            if not possibility:
                print('제거 불가능')
                board[y][x][structure] = structure
            else:
                print('제거 가능')
    for y in range(n + 1):
        for x in range(n + 1):
            for structure in range(2):
                if board[y][x][structure] != -1:
                    answer.append([x, y, structure])
    return answer


# def offsetY(y):
#     return n - y


def isRow(x, y):
    if x < 0 or x > n or y <= 0 or y > n:
        return False
    else:
        return True if board[y][x][1] == 1 else False


def isColumn(x, y):
    if x < 0 or x > n or y < 0 or y > n:
        return False
    else:
        return True if board[y][x][0] == 0 else False


def isPossibleRow(x, y):
    # 한쪽 끝에 기둥이 있는 경우
    if isColumn(x, y - 1) or isColumn(x + 1, y - 1):
        return True
    # 양 쪽 끝에 보가 있는 경우
    if isRow(x - 1, y) and isRow(x + 1, y):
        return True
    return False


def isPossibleColumn(x, y):
    # 바닥인 경우
    if y == 0:
        return True
    # 다른 기둥 위
    if isColumn(x, y - 1):
        return True
    # 보의 한쪽 끝
    if isRow(x - 1, y) or isRow(x, y):
        return True
    return False


build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
               [3, 2, 1, 1]]
n = 5
board = [[[-1,-1] for _ in range(n + 1)] for _ in range(n + 1)]
print(sorted(solution(n, build_frame)))
