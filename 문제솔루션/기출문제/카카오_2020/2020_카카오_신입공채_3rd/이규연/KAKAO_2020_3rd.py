import copy


def print_board(board):
    for i in board:
        for j in i:
            print(j, end=' ')
        print()


def solution(key, lock):
    m = len(key)
    n = len(lock)
    board = init_board(lock, m, n)
    candidate_keys = make_candidate_keys(key, m)
    for si in range(n + m - 1):
        for sj in range(n + m - 1):
            for rot in range(4):
                if put_key(copy.deepcopy(board), candidate_keys[rot], si, sj, m, n):
                    return True
    else:
        return False


def make_candidate_keys(key, m):
    temp = [key]
    for _ in range(3):
        rot_key = [[0 for _ in range(m)] for _ in range(m)]
        for i in range(m):
            for j in range(m):
                rot_key[j][m - 1 - i] = temp[-1][i][j]
        temp.append(rot_key)
    return temp


def put_key(check_board, key, r, c, m, n):
    for i in range(m):
        for j in range(m):
            check_board[r + i][c + j] += key[i][j]
    for i in range(n):
        for j in range(n):
            if check_board[i + m - 1][j + m - 1] != 1:
                return False
    else:
        return True


def init_board(lock, m, n):
    l = n + 2 * (m - 1)
    board = [[0 for _ in range(l)] for _ in range(l)]
    for i in range(n):
        for j in range(n):
            board[i + m - 1][j + m - 1] = lock[i][j]
    return board


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
