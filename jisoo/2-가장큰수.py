import pytest


def solution(numbers):
    numbers = list(map(str, numbers))
    print(len(numbers[0]))
    numbers.sort(key=lambda x: (x[0], x[1 % len(x)], x[2 % len(x)],
                                x[3 % len(x)]), reverse=True)
    print(numbers)
    numbers = "".join(numbers)
    return numbers


@pytest.mark.parametrize("numbers, expected", [
    ([6, 10, 2], "6210"),
    ([3, 30, 34, 5, 9], "9534330")
])
def test_simple(numbers, expected):
    assert solution(numbers) == expected


"""풀이 방법
들어온 숫자들을 string으로 바꿔서 리스트에 넣어준다.
그 리스트를 정렬 한 다음, 하나의 문자열로 붙여준다.

    def solution(numbers):
        numbers = list(map(str, numbers))
        numbers.sort(reverse=True)
        numbers = "".join(numbers)
        return numbers

이렇게 했더니 30이 더 큰 숫자라서 9534303이 나왔다.

자릿수 값으로 비교해주면 될 것 같았다.
도저히 방법이 안떠올라서 다른 사람 코드 참고함

    (x[0], x[1 % len(x)], x[2 % len(x)], x[3 % len(x)])
나머지를 해주는 이유는 자릿수가 넘어가는 경우 때문


이렇게 했는데도 11번 통과가 안된다... 뭐지ㅜㅜㅜㅜ 도와주세옵,,,
"""
