"""
() 이렇게 괄호가 붙어있을 때만 레이저가 있는 경우이므로, 
해당 시점에 sum값에 스택 상에 존재하는 막대기의 개수를 더해준다.
문제에서 확인해보면, 레이저가 아닌 경우에 막대기가 끝나는 시점에 개수를 1개 추가로 세줘야 해서 해당 작업 처리하였다.
"""


def solution(arrangement):
    s = []
    ret = 0
    flag = False
    for idx, a in enumerate(arrangement):
        if a == '(' and arrangement[idx+1] == ')':
            ret += len(s)
            flag = True
            continue
        if a == '(':
            s.append('(')
        else:
            if flag == True:
                flag = False
                continue
            s.pop()
            ret += 1
    return ret


a = '()(((()())(())()))(())'
print(solution(a))
