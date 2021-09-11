def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    reportDict = {}
    for i in report:
        user, ban = i.split(' ')
        if ban in reportDict.keys():
            reportDict[ban].add(user)
        else:
            reportDict[ban] = {user}
    print(reportDict)
    for key, value in reportDict.items():
        if len(value) >= k:
            for ban in value:
                answer[id_list.index(ban)] += 1
    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
# id_list = ["con", "ryan"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 2
print(solution(id_list, report, k))
