"""
participant 배열을 돌면서 dictionary에 존재하면 count를 1씩 증가
completion 배열을 돌면서 dictionary에 element가 있다면, count를 -1 (동명이인을 체크하기 위함)
"""

def solution(participant, completion):
    d = dict()
    for ele in participant:
        if ele in d:
            d[ele] += 1
        else:
            d[ele] = 1
    for ele in completion:
        if ele in d:
            d[ele] -= 1
    answer = ''
    for i in d:
        if d[i] == 1:
            answer = i
    return answer