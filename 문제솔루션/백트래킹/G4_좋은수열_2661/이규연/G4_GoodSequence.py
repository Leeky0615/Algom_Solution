n = int(input())
result = []

# 좋은 수열인지 체크하는 함수
def checkSequence(count):
    for i in range(1, count // 2 + 1):  # 체크해야되는 반복수열의 개수
        if result[count - 2 * i:count - i] == result[count - i:]:  # 반복하는지 안하는지 체크
            return False
    return True


def backTracking(count):
    if count == n:  # 입력값(n)과 단계가 같으면 수열을 출력
        print(*result, sep='')
        return True
    if not checkSequence(count):  # 좋은 수열인지 체크
        return False  # 좋은 수열이 아닌 경우 False를 리턴한다.
    for i in range(1, 4):  # 1,2,3을 순차적으로 체크 -> 크기가 작은 수열을 출력해야하므로 1부터 체크
        result.append(i)  # 결과값에 추가
        if backTracking(count + 1):  # i가 추가된 상태에서 다음 단계 실행
            return True  # 좋은 수열인 경우 True를 리턴 -> 함수 탈출
        result.pop() # 위의 단계에서 False가 리턴되 좋은 수열이 아닐경우 해당 값 제거


backTracking(0)
