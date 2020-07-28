import pytest


def solution(numbers, hand):
    answer = []
    right = 0
    left = 0
    for n in numbers:
        if n in [1, 4, 7]:
            answer.append('L')
            left = n
        elif n in [3, 6, 9]:
            answer.append('R')
            right = n
        else:
            right_check = abs(n-right)
            left_check = abs(n-left)
            if right_check == left_check:
                answer.append(hand[0].upper())
            elif right_check > left_check:
                answer.append("L")
                left = n
            else:
                answer.append("R")
                right = n
    return ''.join(answer)


@pytest.mark.parametrize("numbers, hand, expected", [
    ([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right", "LRLLLRLLRRL")
])
def test_simple(numbers, hand, expected):
    assert solution(numbers, hand) == expected

"""
[ 풀이 방법 ]
- 
"""