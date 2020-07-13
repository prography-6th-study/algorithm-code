import pytest


def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        # i 길이 만큼 문자열 자르기
        temp = [s[j:j+i] for j in range(0, len(s), i)]
        print(temp)

        prev = temp[0]
        prev_idx = 0
        now = 0
        for j in range(1, len(temp)):
            if temp[j] != prev:
                now += j-prev_idx
                prev = temp[j]
                prev_idx = j
                print(i, j, prev)
        now += len(temp)-prev_idx-1
        if now == len(temp):
            now = len(s)
        print(now, answer)
        if now < answer:
            answer = now
    print(answer)
    return 0


@pytest.mark.parametrize("s, expected", [
    ("aabbaccc", 7)
    # ,
    # ('ababcdcdababcdcd', 9),
    # ('abcabcdede', 8),
    # ('abcabcabcabcdededededede', 14),
    # ('xababcdcdababcdcd', 17)
])
def test_simple(s, expected):
    assert solution(s) == expected

"""
[ 풀이 방법 ]
- 모든 경우의 수를 따져서 해봐야 할 것 같다.
"""