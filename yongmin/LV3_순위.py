# 순위
def solution(n, results):
    # key: n번째 선수, value : n번 선수가 이긴/이기지 못한 사람들의 집합
    win, lose = {}, {}
    for i in range(1, n+1):
        win[i], lose[i] = set(), set()

    # 전체 선수들에 대해 반복문을 돈다
    for i in range(1, n+1):
        # 경기 결과에 대해 반복문을 돌면서 win, lose에 이긴 경우와 진 경우를 담는다
        for result in results:
            if result[0] == i:  # i번 선수의 승리
                win[i].add(result[1])   # win[i]에 진 사람(result[1])을 넣는다
            if result[1] == i:   # i번 선수의 패배
                lose[i].add(result[0])   # lose[i]에 i를 이긴 사람(result[0])을 넣는다

        # i를 이긴 사람들(winner)은 i에게 진 사람(win[i])은 반드시 이긴다
        for winner in lose[i]:
            win[winner].update(win[i])

        # i에게 진 사람들(loser)은 i를 이긴 사람들(lose[i])에게는 반드시 진다
        for loser in win[i]:
            lose[loser].update((lose[i]))

    # i번 선수가 이긴 사람의 수와 진 사람의 수를 합쳐 n-1이 되면
    # 이 선수의 순위를 구할 수 있다
    cnt = 0
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1:
            cnt += 1

    return cnt


# test
print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))