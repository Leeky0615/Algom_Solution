def solution(s):
    if len(s) == 1:
        return 1

    result = ""
    length = []

    for i in range(1, len(s) // 2 + 1):
        cnt = 1
        temp_str = s[:i]

        for j in range(i, len(s), i):
            if temp_str == s[j:j + i]:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ""
                result += str(cnt) + temp_str
                cnt = 1
                temp_str = s[j:j + i]
        if cnt == 1:
            cnt = ""
        result += str(cnt) + temp_str
        length.append(len(result))
        result = ""
    return min(length)


s = "aabbaccc"
print(solution(s))
