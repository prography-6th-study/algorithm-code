import pytest


def solution(n, results):
    win = [set() for _ in range(n + 1)]
    lose = [set() for _ in range(n + 1)]
    
    # 초기 세팅
    for w, l in results:
        win[w].add(l)
        lose[l].add(w)
    
    print(win)
    print(lose)

    for i in range(1, n+1):
        # 내가 진 경우를 이긴 상대방한테 넣어준다 -> 항상 이기는 경우를 만들어줌
        for winner in lose[i]:
            # print(i, winner, win[i])
            win[winner].update(win[i])

        # 나를 이긴 사람의 진 경우를 확인해서 항상 지는 경우를 만들어줌
        for loser in win[i]:
            # print(i, loser, lose[i])
            lose[loser].update(lose[i])


    # 총 개수가 n-1인지 확인    
    answer = 0
    for i in range(1, n+1):
        temp = win[i] | lose[i]
        if len(temp) == n-1:
            answer += 1

    return answer


@pytest.mark.parametrize(
    "n, results, expected",
    [
        (5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]], 2),
        (8, [[1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8], [4, 5]], 8)
    ],
)
def test_simple(n, results, expected):
    assert solution(n, results) == expected


"""
[ 풀이 방법 ]
    - 연결된 노드가 n-1개이면 순위를 매길 수 있음
    - 내가 항상 이기는 경우는 자기한테 진 노드가 이긴 경우를 더해주면 됨
    - 내가 항상 지는 경우는 자기를 이긴 노드가 진 경우

    - 처음에 list로 했더니 시간초과 뜸


[ 시간 초과 발생한 코드 ]
def solution(n, results):
    win = [[] for _ in range(n + 1)]
    lose = [[] for _ in range(n + 1)]
    
    # 초기 세팅
    for w, l in results:
        win[w].append(l)
        lose[l].append(w)

    for i in range(1, n+1):
        # 항상 이기는 경우 업뎃
        for w_lose in win[i]:
            win[i] += win[w_lose]
            set(win[i])
        
        # 항상 지는 경우
        for l_win in lose[i]:
            lose[i] += lose[l_win]
            set(lose[i])

    # 총 개수가 n-1인지 확인

    
    answer = 0
    for i in range(1, n+1):
        temp = set(win[i] + lose[i])
        if len(temp) == n-1:
            answer += 1

    return answer
"""
