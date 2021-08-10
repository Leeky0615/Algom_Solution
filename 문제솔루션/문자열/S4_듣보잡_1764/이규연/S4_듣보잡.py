n, m = map(int, input().split())
nArr = {str(input()) for _ in range(n)}
mArr = {str(input()) for _ in range(m)}
result = nArr.intersection(mArr)
print(len(result))
print(*sorted(result), sep='\n')
