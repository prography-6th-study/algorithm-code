"""
방문을 했음을 set을 이용하여 구현하려고 했지만 testcase 2개만 통과하고 나머지는 실패로 뜸.
왜인지 찾아보니 0-1-2 / 3-4 이렇게 영역이 따로 생기는 경우에 마지막에 서로 연결을 해줘야하는데,
각 원소만 방문한 이후에 연결한 것을 체크하지 않고 끝나버리기 때문에 실패로 뜨는 것이라고 한다.

해결을 위해 len(set) == n 까지 while문을 돌며 cost[0], cost[1] 중 하나라도 set에 없는 경우에 
set에 넣어주고 거리를 합산해준다.
"""


def solution_mine(n, costs):
    island = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])
    s1 = s2 = set()
    cnt = 0
    for c in costs:
        s1.add(c[0])
        s2.add(c[1])
        cnt += c[2]
        if s1 == set(island) == s2:
            return cnt


def solution(n, costs):
    island = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])
    s = set()
    cnt = 0
    s.add(0)
    while len(s) != n:
        for c in costs:
            if c[0] in s or c[1] in s:
                if c[0] in s and c[1] in s:
                    continue
                s.add(c[0])
                s.add(c[1])
                cnt += c[2]
                break
    return cnt


n = 4
c = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
print(solution(n, c))
