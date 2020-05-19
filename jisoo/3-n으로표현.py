import pytest


def solution(N, number):
    dp = [0, [N]]
    for i in range(2, 9):
        temp = set([int(str(N) * i)])
        for j in range(1, i // 2 + 1):
            for dp1 in dp[j]:
                for dp2 in dp[i - j]:
                    temp.add(dp1 + dp2)
                    temp.add(dp1 - dp2)
                    temp.add(dp1 // dp2)
                    temp.add(dp2 // dp1)
                    temp.add(dp1 * dp2)
                    # 숫자 확인
                    if number in temp:
                        return i
        # 1보다 작은 값 제거
        temp = [t for t in temp if t > 0]
        dp.append(temp)
    return -1


@pytest.mark.parametrize(
    "N, number, expected", [(5, 12, 4), (5, 31168, -1), (2, 11, 3), (5, 127, 6)],
)
def test_simple(N, number, expected):
    assert solution(N, number) == expected


"""
[ 풀이 방법 ]
    도저히 생각이 안나서 질문 탭을 봤다
    dp에 몇개를 활용하여 만들 수 있는 수를 넣어줬다고 했는데 괜찮은 것 같아서 해봤다
    dp[n] = dp[n-1]*N 한 값들이 들어간다고 생각

    계속 통과가 안돼서 더 찾아봤더니
    dp[4] = dp[1]+dp[3]
    dp[4] = dp[2]+dp[2]
    이런 식으로 해야 한다고 했다.



[ 논의 사항 ]
    - dp 공식? 생각 과정에 대해서 얘기해 보고 싶다


[ 처음 작성한 코드 ]
    def solution(N, number):
        dp = [0, [N]]
        print(dp)
        for i in range(2, 9):
            temp = [int(str(N) * i)]
            for j in dp[i - 1]:
                temp.append(j + N)
                temp.append(j - N)
                temp.append(j // N)
                temp.append(j * N)
            # 1보다 작은 값 제거
            temp = sorted([t for t in set(temp) if t > 0])
            print(i, temp)
            if number in temp:
                print(".")
                return i
            dp.append(temp)
        return -1
"""
