n = int(input())
rd = set()
ru = set()
visit = [False] * n

result = 0


def nqueen(rowNum):
    global rd, ru, visit, result
    if rowNum == n:
        result += 1
        return
    for col in range(n):
        if not (visit[col] or (col - rowNum) in rd or (col + rowNum) in ru):
            visit[col] = True
            rd.add(col - rowNum)
            ru.add(col + rowNum)
            nqueen(rowNum + 1)
            visit[col] = False
            rd.discard(col-rowNum)
            ru.discard(col+rowNum)

nqueen(0)
print(result)