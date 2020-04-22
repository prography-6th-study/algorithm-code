"""
numbers의 모든 element를 str으로 변환하고, key값에 max(x)를 이용해 element에 포함된 숫자가 가장 큰 순으로 정렬되게 했음.
기본 testcase는 통과하는데, 제출했을 때 테스트케이스는 6/11 만 통과(1,2,3,5,6 시간초과로 인한 실패)
아무래도 이중 for문을 돌기 때문에 시간초과 뜨는 것 같은데 어떻게 해야할지.. 인접한 index만 비교하는 것도 문제가 될 수 있다고 생각하는 부분.

+ 혼자 풀다 막혀서 찾아본 다른 사람의 풀이로는, 모든 원소가 1000이하임을 이용해 key값에 x*3 을 넣은 것이 굉장히 신박했다.
"""

import pytest

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: max(x), reverse=True)
    if set(numbers) == {'0'} :
        return "0"
    for i in range(0, len(numbers)+1):
        for j in range(i, len(numbers)):
            if int(numbers[i] + numbers[j]) < int(numbers[j] + numbers[i]):
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return "".join(numbers)

@pytest.mark.parametrize("numbers, expected", [
    ([6, 10, 2], "6210"),
    ([3, 30 ,34 ,5 ,9], "9534330"),
    ([0, 0, 0, 0], "0"),
    ([403, 40], "40403"),
    ([12, 121], "12121"),
    ([2,22,223], "223222"),
    ([21, 212], "21221"),
    ([1000,0,0,0],"1000000"),
    ([12,1213],"121312"),
    ([1],"1"),
    ([0,0], "0"),
    ([5,546], "5546")
])
def test_simple(numbers, expected):
    assert solution(numbers) == expected

