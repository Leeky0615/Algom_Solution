from itertools import permutations


def solution(n, info):
    answer = []
    appeach_dict = {}
    needP = {}
    for i in range(len(info)):
        needP[10 - i] = info[i] + 1
        appeach_dict[10 - i] = info[i]

    score = []
    for i in range(1, n + 1):
        for j in permutations(needP, i):
            sum = 0
            for k in j:
                sum += needP[k]
            if sum == n:
                score.append(j)
    appeach_score = 0
    for key in appeach_dict.keys():
        if appeach_dict[key] != 0:
            appeach_score += key

    for i in score:
        temp = 0
        for j in i:
            temp += score[j]

    return answer


n = 5
info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
print(solution(n, info))
