"""
가장 몸무게가 큰 사람과 작은 사람의 합이 limit를 넘으면 1명만 탈 수 있으니 end 값 -1 한다.
limit보다 작거나 같으면 2명이 탈 수 있으므로, i 값은 +1, end 값은 -1 하여, 2명분이 빠진 것을 표현
"""

def solution(people, limit):
    people.sort()
    ret, i, end = 0, 0, len(people) - 1
    while i <= end:
        if people[i] + people[end] > limit:
            end -= 1
        else:
            i += 1
            end -= 1
        ret += 1 
    return ret