# board = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
board = [[1,2,3],[4,5,6],[7,8,9]]
# skill = [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]


def solution(board, skill):
    answer = len(board) * len(board[0])
    for type, r1, c1, r2, c2, degree in skill:
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if board[i][j] <= 0:
                    state = False
                else:
                    state = True

                if type == 1:
                    board[i][j] -= degree
                else:
                    board[i][j] += degree

                if not state and board[i][j] > 0:
                    answer += 1
                if state and board[i][j] <= 0:
                    answer -= 1
    return answer


print(solution(board, skill))
