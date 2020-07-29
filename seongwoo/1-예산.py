"""
어렵게 생각해서 한참 안 풀리다가
레벨1이 이렇게 어려울리 없다고 생각하여 정렬하고 하나씩 더해서 현재 예산과 일치하는지 확인하여 풀었음.
"""

def solution(d, budget):
    if sum(d) == budget:
        return len(d)
    else:
        s = 0
        idx = 0
        for i in sorted(d):
            if s + i > budget:
                break
            else:
                s += i
                idx += 1
        return idx