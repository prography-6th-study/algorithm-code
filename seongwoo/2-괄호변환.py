"""
문제 설명 그대로 구현하면 되는 문제였는데, 엄청 헤맸다. 어느 정도 다른 사람 코드 참조.
u, v 로 문자열을 분리하는 과정에서 재귀적으로 v에 변환 과정을 반복해야되는데, input parameter로 들어오는 값은 p이다 보니
자꾸 복잡하게 풀게 되었다.
이것은 재귀이기 때문에 u, p로 분리하여 p를 계속 갱신하면 쉽게 풀 수 있던 문제였다. 
"""

import pytest

def check(string):
    li = []
    for s in string:
        if s == '(':
            li.append('(')
        else:
            if li == []:
                return False
            else:
                li.pop()
    return True
    
def split(p):
    idx = 0
    temp = []
    while True:
        temp.append(p[idx])
        idx += 1
        if temp.count('(') == temp.count(')'):
            break
    return p[:idx], p[idx:]

def reverse(u):
    re_s = ""
    for i in u:
        if i == '(':
            re_s += ')'
        else:
            re_s += '('
    return re_s

def solution(p):
    ret = ""
    while p != "":
        u, p = map(str, split(p))
        if check(u) == True:
            ret += u
        else:
            ret += '(' + solution(p) + ')' + reverse(u[1:-1])
            break
    return ret
    

@pytest.mark.parametrize("p, expected", [
    ("(()())()", "(()())()"),
    (")(", "()"),
    ("()))((()", "()(())()")
])
def test_simple(p, expected):
    assert solution(p) == expected