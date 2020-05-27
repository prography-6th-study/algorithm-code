def solution(n, results):
    winTo, loseTo = {}, {}

    winner = 0
    loser = 1

    for i in range(1, n+1):
        winTo[i], loseTo[i] = set(), set()

    for i in range(1, n+1):
        for result in results:
            if result[winner] == i:
                winTo[i].add(result[loser])
            if result[loser] == i:
                loseTo[i].add(result[winner])

        for w in loseTo[i]: #선수1에게 진 사람은 반드시 선수1에게 이긴 사람에게 진다
            winTo[w].update(winTo[i])

        for l in winTo[i]: #선수1에게 이긴 사람은 반드시 선수1에게 진 사람을 이긴다
            loseTo[l].update(loseTo[i])
            
        answer = 0
    for i in range(1, n+1):
        if len(loseTo[i]) + len(winTo[i]) == n-1:
            answer+=1
    return answer


"""풀이방법
처음 생각:
선수별로 경기 수를 세서 n-1인 사람을 찾으면 된다
- 예시의 5번 선수 같은 경우는 찾을 수 없음

중요 조건
선수1에게 이긴 사람은 반드시 선수1에게 진 사람을 이긴다
선수1에게 진 사람은 반드시 선수1에게 이긴 사람에게 진다

바꾼 생각:
선수1에게 진 사람 + 이긴 사람 == n-1 이면 순위를 알아낼 수 있다
"""