n = int(input())
arr = []
dist = []

for i in range(n):
    temp = int(input())
    if i != 0:
        dist.append(abs(temp - arr[i - 1]))
    arr.append(temp)


def get_gcd(a, b):
    if a % b == 0:
        return b
    else:
        return get_gcd(b, a % b)


gcd = get_gcd(dist[0], dist[1])
if n > 3:
    for i in dist[2:]:
        gcd = get_gcd(gcd, i)

result = 0
for i in dist:
    result += (i // gcd) - 1

print(result)
