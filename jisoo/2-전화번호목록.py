import pytest


def solution(phone_book):
    phone_book.sort()
    for a, b in zip(phone_book, phone_book[1:]):
        if a in b:
            return False
    return True


@pytest.mark.parametrize("phone_book, expected", [
    (['119', '97674223', '1195524421'], False),
    (['123', '456', '789'], True),
    (['12', '123', '1235', '567', '88'], False)
])
def test_simple(phone_book, expected):
    assert solution(phone_book) == expected


"""
zip이라는 함수를 이용해서 2개씩 비교하게 했다.
a가 b에 포함되어 있으면 False 리턴
"""
