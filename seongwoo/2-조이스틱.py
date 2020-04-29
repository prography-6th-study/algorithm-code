""" 
위아래 조작하는 값은 쉽게 찾았는데
좌우로 조작하는 것에서 최소값을 찾는 것에서 막혀서, 해당 부분은 찾아서 추가했음.
"""

import pytest

def solution(name):
    cnt = 0 
    idx = 0
    name = list(name)
    while True:
        right, left = 1, 1
        n = ord(name[idx])
        if n != 65:
            if n <= 78:
                cnt += n - 65
            else:
                cnt += 91 - n
            name[idx] = 'A'
        if name == ['A'] * len(name):
            break
        else:
            for i in range(1, len(name)):
                if name[idx + i] == 'A':
                    right += 1
                else: break
                if name[idx - i] == 'A':
                    left += 1
                else: break
            cnt += min(right, left)
            idx = (idx + right) if min(right, left) == right else (idx - left)
    return cnt

@pytest.mark.parametrize("name, expected", [
    ("JEROEN", 56),
    ("JAN", 23),
    ("JAZ", 11)
])
def test_simple(name, expected):
    assert solution(name) == expected