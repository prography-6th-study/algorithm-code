"""
각 스테이지에 대하여 실패한 경우와 성공한 경우에 대한 dictionary의 value를 1씩 더해주면서 체크했고,
실패율을 계산할 때 0으로 나누는 것만 고려하고 이후 정렬된 인덱스 값들을 반환하였다.
"""


def solution(N, stages):
    fd, sd = dict(), dict()
    ret, ans = [], []
    for i in range(1, N + 1):
        fd[i], sd[i] = 0, 0
        for j in stages:
            if i == j:
                fd[i] += 1
                sd[i] += 1
            elif i < j:
                sd[i] += 1
    for j in range(1, N + 1):
        if sd[j] == 0:
            ret.append([0, j])
        else:
            ret.append([fd[j] / sd[j],  j])
    ret.sort(key=lambda x: x[0], reverse=True)

    for i in range(N):
        ans.append(ret[i][1])
    return ans


n = 8
s = [1, 2, 3, 4, 5, 6, 7]

print(solution(n, s))
