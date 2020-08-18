"""
스택을 이용하여 스택[-1] 이 다음 문자열과 같다면 pop, 아닌 경우에 push 하는 것으로 구현.
"""

def solution(s):
    t = []
    for i in s:
        if not t:
            t.append(i)
        elif t[-1] == i:
            t.pop()
        else:
            t.append(i)
    return 1 if len(t) == 0 else 0
        
