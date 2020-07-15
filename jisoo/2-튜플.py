import pytest


def solution(s):
    s = s.split('},')
    num_list = []
    for now in s:
        # 괄호 제거
        now = now.replace('{', '')
        now = now.replace('{{', '')
        now = now.replace('}}', '')
        temp = now.split(",")
        temp = list(map(int, temp))
        num_list.append(temp)

    num_list.sort(key=len)

    answer = []
    for num in num_list:
        for n in num:
            if n in answer:
                continue
            answer.append(n)
    return answer



@pytest.mark.parametrize("s, expected", [
    ("{{2},{2,1},{2,1,3},{2,1,3,4}}", [2, 1, 3, 4]),
    ("{{1,2,3},{2,1},{1,2,4,3},{2}}", [2, 1, 3, 4]),
    ("{{20,111},{111}}", [111, 20])
])
def test_simple(s, expected):
    assert solution(s) == expected

"""
[ 풀이 방법 ]
- 
"""