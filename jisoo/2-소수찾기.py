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


"""
from itertools import permutations
def check_prime(arr, length):
    sum = 0
    arr = set(map(int, arr))
    check = [False]*2+[True]*(max(arr)-1)
    for a in arr:
        if check[a] is False or len(str(a)) < length:
            continue
        for i in range(2, a+1):
            for j in range(2, (a//i)+1):
                check[i*j] = False
        if check[a] is True:
            print(a)
            sum += 1
    return sum


def solution(numbers):
    answer = 0
    for i in range(1, len(numbers)+1):
        num_list = set(map(''.join, permutations(numbers, i)))
        answer += check_prime(num_list, i)
    return answer
"""
