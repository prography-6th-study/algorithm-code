import pytest

# def make_array(num):
    


def solution(n, arr1, arr2):
    map1 = []
    map2 = []
    # 자릿수 맞춰서 넣어주기
    for num1, num2 in zip(arr1, arr2):
        binary = bin(num1)
        binary = str(binary[2:]).zfill(n)
        map1.append(binary)

        binary = bin(num2)
        binary = str(binary[2:]).zfill(n)
        map2.append(binary)

    answer = []
    for ma1, ma2 in zip(map1, map2):
        temp = []
        for m1, m2 in zip(ma1, ma2):
            if m1 == '0' and m2 == '0':
                temp.append(' ')
                continue
            temp.append('#')
        answer.append(''.join(temp))
    return answer


@pytest.mark.parametrize("n, arr1, arr2, expected", [
    (5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28], ["#####", "# # #", "### #", "#  ##", "#####"])
])
def test_simple(n, arr1, arr2, expected):
    assert solution(n, arr1, arr2) == expected

"""
[ 풀이 방법 ]
- 
"""