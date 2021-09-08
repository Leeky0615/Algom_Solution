n = int(input())
rd = set() # 오른쪽 아래 대각선 -> col - rowNum의 값이 똑같음
ru = set() # 오른쪽 위 대각선 -> col + rowNum의 값이 똑같음
visit = [False] * n

result = 0

def nqueen(rowNum):
    global rd, ru, visit, result
    if rowNum == n:
        result += 1
        return
    for col in range(n):  # 모든 열 반복
        # 퀸이 놓여 있거나, 오른쪽 아래 대각선 이거나, 오른쪽 위 대각선인 경우가 아닐때만
        if not (visit[col] or (col - rowNum) in rd or (col + rowNum) in ru):
            # 퀸을 놓고 대각선 경로를 추가한다.
            visit[col] = True
            rd.add(col - rowNum)
            ru.add(col + rowNum)
            # 다음 행 실행
            nqueen(rowNum + 1)
            # 백트래킹
            visit[col] = False
            rd.discard(col - rowNum)
            ru.discard(col + rowNum)

nqueen(0)
print(result)
