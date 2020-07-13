import pytest


def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        # i 길이 만큼 문자열 자르기
        temp = [s[j:j+i] for j in range(0, len(s), i)]

        prev = temp[0]
        now = 0
        count = 0
        for j in range(len(temp)):
            if temp[j] == prev:
                count += 1
            # 다른 문자열이 나온 경우
            else:
                if count == 1:
                    count = 0
                else:
                    # 겹치는 개수의 자릿수를 더해주기
                    count = len(str(count))
                now += count + len(prev)
                prev = temp[j]
                count = 1

        # 나머지 문자열 처리
        if count == 1:
            count = 0
        else:
            count = len(str(count))
        now += count + len(temp[-1])
        
        # 최소값 구하기
        if now < answer:
            answer = now
    return answer


@pytest.mark.parametrize("s, expected", [
    ("aabbaccc", 7),
    ('ababcdcdababcdcd', 9),
    ('abcabcdede', 8),
    ('abcabcabcabcdededededede', 14),
    ('xababcdcdababcdcd', 17),
    ('AZAAAZ', 5),
    ('AABAAAAAAABBB', 7),
    ('ZZBBABBAA', 9),
    ('aaaaaaaaaabbb', 5)
])
def test_simple(s, expected):
    assert solution(s) == expected

"""
[ 풀이 방법 ]
- 모든 경우의 수를 따져서 해봐야 할 것 같다.
- 겹치는 수의 개수의 자릿수를 더해줘야 한다
"""