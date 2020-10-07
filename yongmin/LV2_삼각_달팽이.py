def solution(n):
    t = [[0] * i for i in range(1, n + 1)]  # 삼각형 초기화
    x, y = -1, -0  # 삼각형(2차원 리스트)의 인덱스
    num = 1  # 삼각형에 들어갈 값
    # 1부터 n까지
    for i in range(n):
        # i부터 n까지
        for j in range(i, n):
            # 삼각형의 왼쪽
            if i % 3 == 0:
                x += 1
            # 삼각형의 밑변
            elif i % 3 == 1:
                y += 1
            # 삼각형의 오른쪽
            elif i % 3 == 2:
                x -= 1
                y -= 1
            t[x][y] = num
            num += 1

    answer = []
    for arr in t:
        answer += arr
    return answer


# test
print(solution(4))
print(solution(5))
print(solution(6))