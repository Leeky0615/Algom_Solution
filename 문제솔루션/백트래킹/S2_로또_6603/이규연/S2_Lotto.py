from itertools import combinations

while True:
    inputs = list(map(int, input().split()))
    k = inputs[0]
    if k == 0:
        break
    s = inputs[1:]
    for i in combinations(s, 6):
        print(*i)
    print()
