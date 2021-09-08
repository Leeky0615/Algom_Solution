def solution(p):
    if len(p) == 0 or check_correct(p):
        return p
    u, v = divide(p)
    if check_correct(u):
        return u + solution(v)
    return "(" + solution(v) + ")" + "".join(flip(x) for x in u[1:-1])


def divide(p):
    i = 2
    while i < len(p):
        if p[:i].count('(') == i // 2:
            return p[:i], p[i:]
        else:
            i += 2
    return p, ""


def flip(x):
    return ")" if x == "(" else "("


def check_correct(p):
    flag = 0
    for i in p:
        if i == '(':
            flag += 1
        else:
            flag -= 1
        if flag < 0:
            return False
    else:
        if flag == 0:
            return True


p = "()))((()"
print(solution(p))
