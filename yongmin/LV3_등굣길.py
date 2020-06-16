def solution(m, n, puddles):
    # 길 초기화 (인덱스 맞춰주기 위해 가로+1, 세로+1)
    roads = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                roads[j][i] = 1  # 시작점
            if [j, i] in puddles:
                continue  # 물웅덩이는 건너뛴다

            # 현재위치까지 도달할 수 있는 경우의 수 =
            #   위쪽에서 들어오는 경우의 수 + 왼쪽에서 들어오는 경우의 수
            roads[i][j] += (roads[i-1][j] + roads[i][j-1])

    return roads[-1][-1] % 1000000007


# test
print(solution(4, 3, [[2,2]]))