import pytest


def solution(heights):
    heights.reverse()
    print(heights)
    leng = len(heights)
    answer = [0] * leng
    for idx, h in enumerate(heights):
        for i in range(idx+1, leng):
            if h < heights[i]:
                answer[idx] = leng-i
                break
    answer.reverse()
    return answer


@pytest.mark.parametrize("heights, expected", [
    ([6, 9, 5, 7, 4],  [0, 0, 2, 2, 4]),
    ([3, 9, 9, 3, 5, 7, 2],  [0, 0, 0, 3, 3, 3, 6]),
    ([1, 5, 3, 6, 7, 6, 5],  [0, 0, 2, 0, 0, 5, 6])
])
def test_simple(heights, expected):
    assert solution(heights) == expected


"""풀이 방법
일단 리스트를 reverser 해서 for문을 돈다.
자신 보다 큰 값을 만나면, 그게 몇 번 탑인지 기록하고 넘어간다.
"""
