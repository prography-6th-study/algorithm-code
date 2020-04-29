import pytest
from itertools import permutations


def solution(numbers):
    # 조합으로 숫자 만들기
    num = []

    numbers = list(numbers)
    for idx in range(len(numbers)):
        num += set(map(''.join, permutations(numbers, idx+1)))
    num = sorted(list(set(map(int, num))))
    print(num)

    answer = 0
    # 소수 체크 (에라토스테네스의 채)
    for n in num:
        if n < 2:
            continue
        check = True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                check = False
                break
        if check:
            answer += 1
    return answer


@pytest.mark.parametrize("numbers, expected", [
    ("17", 3),
    ("011", 2)
])
def test_simple(numbers, expected):
    assert solution(numbers) == expected


""" 풀이방법
조합으로 숫자 리스트를 만들고 소수인지 확인해줌
소수 확인 범위는 루트를 씌운 값까지만 나눠지는지 확인하면 된다.
"""
