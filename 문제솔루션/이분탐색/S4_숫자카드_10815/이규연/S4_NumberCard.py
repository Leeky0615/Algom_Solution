from bisect import bisect_right, bisect_left
import sys

n = int(sys.stdin.readline())
nCards = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
mCards = list(map(int, sys.stdin.readline().split()))
for i in mCards:
    if bisect_left(nCards, i) != bisect_right(nCards, i):
        print(1, end=' ')
    else:
        print(0, end=' ')
