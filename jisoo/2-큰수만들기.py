import pytest


def solution(number, k):
    answer = []
    count = len(number) - k
    for n in number:
        while answer and answer[-1] < n and k > 0:
            answer.pop()
            k -= 1
        answer.append(n)
    return ''.join(answer[:count])



@pytest.mark.parametrize("number, k, expected", [
    ("1924", 2, "94"),
    ("1231234", 3, "3234"),
    ("4177252841", 4, "775841"),
    ('1111', 2, '11')
])
def test_simple(number, k, expected):
    assert solution(number, k) == expected

"""
[ 풀이 방법 ]
- combination을 이용해서 풀었더니 시간초과 발생
"""