import pytest
from collections import deque


def solution(priorities, location):
    wait = deque((value, idx) for idx, value in enumerate(priorities))

    max_num = max(wait)
    count = 1
    done = []
    while wait:
        now = wait.popleft()
        # 뒤에 큰 값이 있는 경우
        if max_num[0] > now[0]:
            wait.append(now)
        # 뒤에 큰 값이 없는 경우 done에 넣어줌
        else:
            done.append(now)
            if not wait:
                break
            max_num = max(wait)
        print(wait)
    
    answer = 0
    for d in done:
        answer += 1
        if d[1] == location:
            break
    
    return answer



@pytest.mark.parametrize("priorities, location, expected", [
    ([2, 1, 3, 2], 2, 1),
    ([1, 1, 9, 1, 1, 1], 0, 5)
])
def test_simple(priorities, location, expected):
    assert solution(priorities, location) == expected