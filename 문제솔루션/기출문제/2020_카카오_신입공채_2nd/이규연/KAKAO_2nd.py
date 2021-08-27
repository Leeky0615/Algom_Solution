from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for c in course:  # 코스의 개수
        availableCourse = []
        for o in orders:  # 모든 주문에 대해서
            comb = combinations(sorted(o), c)  # 코스의 개수만큼 조합.
            availableCourse += comb  # 가능한 모든 코스에 대해 더해줌.
        courseCount = Counter(availableCourse)  # 가능한 코스에 대해서 개수를 세어줌. 내림차순정렬까지.
        if len(courseCount) != 0 and max(courseCount.values()) != 1:  # 가능한 코스의 개수가 없으면 안됨. & 메뉴의 조합이 2개 이상은 되어야함.
            for i in courseCount:  # count 된 배열에서
                if courseCount[i] == max(courseCount.values()):  # value값(코스의 개수)이 가장 많은 코스의 개수와 똑같다면
                    answer.append(''.join(i))  # answer에 더해주기
    return sorted(answer)


orders1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course1 = [2, 3, 4]
orders2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course2 = [2, 3, 5]
orders3 = ["XYZ", "XWY", "WXA"]
course3 = [2, 3, 4]

print(solution(orders3, course3))
