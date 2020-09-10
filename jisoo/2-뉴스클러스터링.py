from collections import Counter

import pytest


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    str1_list = []
    str2_list = []
    for i in range(len(str1)):
        str1_list.append(str1[i:i+2])
    for i in range(len(str2)):
        str2_list.append(str2[i:i+2])

    new_str1 = []
    for str1 in str1_list:
        if str1.isalpha() and len(str1) == 2:
            new_str1.append(str1)
    new_str2 = []
    for str2 in str2_list:
        if str2.isalpha() and len(str2) == 2:
            new_str2.append(str2)

    if len(new_str1) == 0 and len(new_str2) == 0:
        return 65536

    intersection = Counter(new_str1) & Counter(new_str2)
    union = Counter(new_str1) | Counter(new_str2)
    return int(sum(intersection.values())/sum(union.values())*65536)


@pytest.mark.parametrize("str1, str2, expected", [
    ("FRANCE", "french", 16384),
    ("handshake", "shake hands", 65536),
    ("aa1+aa2", "AAAA12", 43690),
    ("E=M*C^2", "e=m*c^2", 65536)
])
def test_simple(str1, str2, expected):
    assert solution(str1, str2) == expected

"""
[ 풀이 방법 ]
- 
"""