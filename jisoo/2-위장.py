import pytest


def solution(clothes):
    category = {}
    for value, key in clothes:
        print(value, key)
        if key in category:
            category[key] += 1
        else:
            category[key] = 1

    answer = 1
    for value in category.values():
        answer *= (value+1)
    return answer - 1
    


@pytest.mark.parametrize("clothes, expected", [
    ([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]], 5),
    ([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]], 3)
])
def test_simple(clothes, expected):
    assert solution(clothes) == expected


"""
[ 풀이방법 ]
    - 해쉬를 이용해서 각 옷이 몇개가 존재한지 계산해 준다
    - 그 다음에 안 입는 경우를 생각해서 +1
    - 순열로 계산을 해준다
"""
