for _ in range(int(input())):
    p = input()
    s = int(input())
    result = input()[1:-1].split(',')
    if s == 0:
        result = []
    rStatus = False
    start = 0
    end = 0
    for i in p:
        if i == 'R':
            rStatus = not rStatus
        elif i == 'D' and rStatus:
            end += 1
        elif i == 'D' and not rStatus:
            start += 1

    if start + end <= s:
        result = result[start:s - end]
        if rStatus:
            print('[' + ','.join(result[::-1]) + ']')
        else:
            print('[' + ','.join(result) + ']')
    else:
        print("error")
