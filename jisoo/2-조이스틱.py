import pytest


def solution(name):
    name = list(name)
    base = ["A"] * len(name)

    idx = 0
    answer = 0

    while True:
        # 알파벳 변경
        if base[idx] != name[idx]:
            # A로 바꾸는게 빠른 경우
            if abs(ord(name[idx]) - ord("A")) < 14:
                answer += ord(name[idx]) - ord("A")
            else:
                answer += ord("Z") - ord(name[idx]) + 1
            name[idx] = 'A'

        # 문자열이 같아지면 멈춘다
        if base == name:
            break

        # 위치이동
        for i in range(1, len(name)):
            if name[idx + i] != "A":
                idx += i
                answer += i
                break
            if name[idx - i] != "A":
                idx -= i
                answer += i
                break

    return answer


@pytest.mark.parametrize(
    "name, expected", [("JEROEN", 56), ("JAN", 23), ("BBABA", 6), ("BBAABAAAAB", 12)]
)
def test_simple(name, expected):
    assert solution(name) == expected


""" 풀이 방법
처음 알파벳을 바꿀 때는 A와 가까운지 Z와 가까운지 찾아낸다.
그 다음 바꾼 name은 'A'로 표시한다. 처음에는 base를 name처럼 바꿨는데 시간 초과 났음

인덱스 이동은 가장 가까이 있는 A가 아닌 알파벳으로 가는 방법을 찾아야한다.
오른쪽, 왼쪽으로 이동하면서 가까이 있는 알파벳을 찾아 인덱스를 구해준다.
"""
