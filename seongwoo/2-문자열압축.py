"""
처음에 문제를 잘못 이해해서 aabbbcc -> 2a3b2c 로 변환하는 알고리즘으로 풀어서 틀렸음.
문제를 다시 이해하고 풀었는데, 몇몇 테케에서 제대로 안 짤리는 문제 + 마지막에 자르고 남는 문자열 처리에서 오류가 있었다.
결국에 블로그에서 다른 사람 풀이를 보고 풀게 되었는데,
range() 함수의 3번째 parameter인 step을 사용했으면 복잡하게 안 풀어도 되었던 문제였다.

+ 5번 테스트케이스는 "a" 같은 경우임
"""

import pytest

def solution_mine(s):
    l = len(s)
    idx = 0 
    ret = ""
    part_len = 0
    first = True
    while idx < len(s):
        cnt = 0
        last = s[idx:idx + part_len]
        if first == True:
            for i in range(1, l // 2 + 1):
                if s[idx:idx + i] == s[idx + i:idx + 2 * i]:
                    last = s[idx:idx + i]
                    part_len = i
                    cnt += 2
                    first = False
            if part_len == 0:
                if idx == 0:
                    return len(str(s))
                part_len = 1
                idx += 1
            else:
                idx += 2 * part_len
        while s[idx: idx + part_len] == last:
            cnt += 1
            idx += part_len
        if cnt == 0:
            ret += s[idx]
            idx += 1
        else:
            ret += str(cnt) + last
    return len(ret)

def solution(s):
    answer = float('inf')
    for i in range(1, len(s) // 2 + 1): # 잘리는 개수
        ret = ""
        cnt = 1
        last = s[0:i]
        for idx in range(i, len(s) + i, i): # 실제 인덱스, range 함수 안에 step을 이용해 일정 갯수만큼 split
            if last == s[idx:idx + i]:
                cnt += 1
            else:
                if cnt != 1:
                    ret += str(cnt) + last
                else:
                    ret += last
                last = s[idx:idx + i]
                cnt = 1
        answer = min(answer, len(ret))
    return min(answer,len(s))
    


@pytest.mark.parametrize("s, expected", [
    ("aabbaccc", 7),
    ("ababcdcdababcdcd"	, 9),
    ("abcabcdede", 8),
    ("abcabcabcabcdededededede", 14),
    ("xababcdcdababcdcd", 17),
    ("a",1)
])
def test_simple(s, expected):
    assert solution(s) == expected