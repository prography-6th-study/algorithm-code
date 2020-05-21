"""
선수 A가 있을 때, (A를 이긴 사람 수) + (A에게 진 사람 수) ==  n-1 가 만족하면,
해당 선수는 정확하게 순위를 매길 수 있는 선수이다.
"""

def solution(n, results):
    wins, loses = {}, {} # A가 이긴 사람들 / A가 진 사람들
    for i in range(1, n + 1):
        wins[i], loses[i] = set(), set()
    for i in range(1, n + 1):
        for battle in results:
            if battle[0] == i: # i가 이긴 사람을 업데이트
                wins[i].add(battle[1]) 
            if battle[1] == i: # i가 진 사람을 업데이트
                loses[i].add(battle[0])
        for winner in loses[i]: # i가 진 사람은 무조건 i에게 이긴다.
            wins[winner].update(wins[i])
        for loser in wins[i]: # i가 이긴 사람은 무조건 i에게 진다.
            loses[loser].update(loses[i])
    cnt = 0
    for i in range(1, n + 1):
        if len(wins[i]) + len(loses[i]) == n - 1: 
            cnt += 1
    return cnt

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))