def solution(new_id):
    answer = ''

    # STEP 1 : 대문자 -> 소문자
    new_id = new_id.lower()
    # print('STEP1 :', new_id)

    # STEP 2: 소문자, 숫자, 빼기, 밑줄, 마침표 제외 모든 문자 제거
    whiteList = ['.', '-', '_']
    for i in new_id:
        if i in whiteList or i.isdecimal() or (i.isalpha() and i.islower()):
            answer += i
    # print('STEP2 :', answer)

    # STEP 3: 마침표가 2개 이상 연속 있는 경우 하나로 치환.
    dotCount = 0
    temp = ''
    for i in answer:
        if i != '.':
            temp += i
            dotCount = 0
        else:
            if dotCount == 0:
                temp += i
            dotCount += 1
    answer = temp
    # print('STEP3 :', answer)

    # STEP 4: 마침표가 처음이나 끝에 위치한다면 제거 합니다.
    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    # print('STEP4 :', answer)

    # STEP 5: 빈문자열이라면 a를 대입.
    if not answer:
        answer += 'a'
    # print('STEP5 :', answer)

    # STEP 6 : 문자열 길이 16이상이면 15까지 자르기 & 마지막이 마침표라면 그것도 제거
    endPoint = 15
    if answer[:endPoint][-1] == '.':
        endPoint -= 1
    answer = answer[:endPoint]
    # print('STEP6 :', answer)

    # STEP 7 : 길이가 3보다 작으면 마지막 문자를 길이가 3이될때 까지 붙인다.
    while len(answer) < 3:
        answer += answer[-1]
    # print('STEP7 :', answer)


    return answer


print(solution(input()))

