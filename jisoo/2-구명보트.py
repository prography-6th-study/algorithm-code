import pytest


def solution(people, limit):
    people.sort()
    answer = 0
    i = 0
    j = len(people)-1
    
    while i <= j:
        # 둘 다 태울 수 있는 경우
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        answer += 1
    return answer

@pytest.mark.parametrize("people, limit, expected", [
    ([70, 50, 80, 50], 100, 3)
    # ,
    # ([70, 80, 50], 100, 3)
])
def test_simple(people, limit, expected):
    assert solution(people, limit) == expected

"""
[ 풀이 방법 ]
- 
"""