import math


def solution(n, k):
    answer = 0
    tNum = trans_num(n, k)
    candidate = str(tNum).split('0')
    for i in candidate:
        if i and int(i) != 1 and is_prime(int(i)):
            answer += 1
    return answer


def trans_num(n, k):
    temp = "0123456789ABCDEF"
    quotient, remainder = divmod(n, k)
    if quotient:
        return trans_num(quotient, k) + temp[remainder]
    else:
        return temp[remainder]


def is_prime(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

print(solution(437674, 3))
print(solution(110011, 10))
