import pytest

def check(p):
    stack = []
    if p[0] == ')':
        return False
    for now in p:
        if now == '(':
            stack.append('(')
        else:
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
    return True

def divide(w):
    u = []
    v = []
    open_count = 0
    close_count = 0
    if w == "":
        return ""

    for idx, now in enumerate(w):
        if now == '(':
            open_count += 1
        else:
            close_count += 1
        if open_count == close_count:
            u = w[:idx+1]
            v = w[idx+1:]
            break
    print(w, u, v)
    if check(u):
        print("u는 진짜다", v)
        v = divide(v)
        return u+v
    else:
        temp = '(' + divide(v) + ')'
        print(temp, 'temp')
        u = u[1:-1]
        for now in u:
            if now == '(':
                temp += ')'
            else:
                temp += '('
        return temp
        
    
def solution(p):
    if p == "":
        return p
    answer = divide(p)
    return answer



@pytest.mark.parametrize("p, expected", [
    ("(()())()", "(()())()"),
    (')(', '()'),
    ("()))((()", "()(())()")
])
def test_simple(p, expected):
    assert solution(p) == expected

"""
[ 풀이 방법 ]
- 
"""