import pytest


def solution(msg):
    dictionary = dict()
    last_index = 26
    for idx, alphabet in enumerate([chr(i) for i in range(ord('A'), ord('A') + 26)]):
        dictionary[alphabet] = idx + 1

    answer = []

    while True:
        length = len(msg)
        for idx in range(length):
            if idx == 0:
                temp = msg
            else:
                temp = msg[:-idx]
            if temp in dictionary:
                answer.append(dictionary[temp])

                last_index += 1
                dictionary[msg[:length - idx + 1]] = last_index

                msg = msg[length-idx:]
                break
        if length == 0:
            break

    return answer


@pytest.mark.parametrize("msg, expected", [
    ("KAKAO", [11, 1, 27, 15]),
    ("TOBEORNOTTOBEORTOBEORNOT", [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]),
    ("ABABABABABABABAB", [1, 2, 27, 29, 28, 31, 30])
])
def test_simple(msg, expected):
    assert solution(msg) == expected

"""
[ 풀이 방법 ]
- A~Z까지 dict로 만들어놓고 msg를 뒤에서 부터 보면서(문자열이 긴 거 먼저 확인해야 하니까) 일치하는 문자열을 찾는다.
없으면 dict에 추가
"""