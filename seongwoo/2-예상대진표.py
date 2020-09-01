"""
한 라운드가 지날 때마다 (해당 참가자 번호 / 2) 에서 소수점을 올림한 값으로 참가자 번호를 재설정시켰음.

처음에는 50%의 테스트케이스만 통과하였음. 그 이유는 재귀에서 탈출 조건을 잘못 설정했던 것 때문.
원래 a == 1 and b == 2 일때 탈출하도록 설정하였는데, 다른 값으로 만나는 경우도 있는 것 같음.
조건을 해당 시점이 아니라 a == b 로 설정을 해야 제대로 탈출함.
"""

import math

def dfs(a, b):
    global cnt
    if a == b:
        return
    a = math.ceil(a / 2)
    b = math.ceil(b / 2)
    cnt += 1
    dfs(a, b)


cnt = 0
def solution(n, a, b):
    if a > b:
        a, b = b, a
    dfs(a, b)
    return cnt
    
print(solution(8, 4, 7))
