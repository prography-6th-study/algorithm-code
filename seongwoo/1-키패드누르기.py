"""
뭔가 더 간결하게 풀 수 있을 것 같기도 하지만
나는 딕셔너리 + [2,5,8,0] 의 경우에 나와있는 조건을 그대로 구현하여 풀었다.
"""

import pytest

def solution(numbers, hand):
    ret, d = "", dict() 
    right, left= (3, 0), (3, 2)
    d[1] = 'L'
    d[4] = 'L'
    d[7] = 'L'
    d[3] = 'R'
    d[6] = 'R'
    d[9] = 'R'

    for n in numbers:
        if n in [2,5,8,0]:
            pos = ([2, 5, 8, 0].index(n), 1)
            right_dist = abs(pos[1] - right[1]) + abs(pos[0] - right[0])
            left_dist = abs(pos[1] - left[1]) + abs(pos[0] - left[0])
            if right_dist < left_dist:
                right = pos
                ret += 'R'
            elif right_dist > left_dist:
                left = pos
                ret += 'L'
            else:
                if hand == "right":
                    right = pos
                    ret += 'R'
                else:
                    left = pos    
                    ret += 'L'
        else:
            ret += d[n]
            if n in [1,4,7]:
                left = ([1,4,7].index(n),0)
            else:
                right = ([3,6,9].index(n),2)
    return ret

@pytest.mark.parametrize("numbers, hand, expected", [
    ([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right", "LRLLLRLLRRL"),
    ([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left", "LRLLRRLLLRR"),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right", "LLRLLRLLRL"),
])
def test_simple(numbers, hand, expected):
    assert solution(numbers, hand) == expected