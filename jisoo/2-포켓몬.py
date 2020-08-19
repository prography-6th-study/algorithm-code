import pytest

def solution(nums):
    max_num = len(set(nums))
    if len(nums) // 2 < max_num:
        max_num = len(nums) // 2
    return max_num

    # return min(len(set(nums)), len(nums)//2)


@pytest.mark.parametrize("nums, expected", [
    ([3,1,2,3], 2),
    ([3,3,3,2,2,4], 3),
    ([3,3,3,2,2,2], 2)
])
def test_simple(nums, expected):
    assert solution(nums) == expected

"""
[ 풀이 방법 ]
- 리스트 안에 겹치지 않는 수와 뽑을 수 있는 수만 비교하면 되는 간단한 문제
"""