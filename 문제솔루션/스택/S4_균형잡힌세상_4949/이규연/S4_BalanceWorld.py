while True:
    line = input()
    if line == ".":
        break
    sStatus = 0
    mStatus = 0
    for i in line:
        if i == '(':
            sStatus += 1
        if i == '[':
            mStatus += 1
        if i == ')':
            sStatus -= 1
        if i == ']':
            mStatus -= 1
    if sStatus == 0 and mStatus == 0:
        print("yes")
    else:
        print("no")

