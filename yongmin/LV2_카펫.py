def solution(brown, yellow):
    total = brown + yellow  # 격자의 총 개수
    for i in range(3, total):
        # total = 가로*세로 이므로 나누어 떨어지는 수를 찾는다
        if total % i == 0:
            # 가로, 세로
            a, b = (total // i), i
            if a < b:  # 가로 >= 세로
                continue
            # brown을 둘레라고 생각하면
            # 가로길이 * 2, 세로길이 * 2
            # -2 는 세로 길이에서 위아래로 겹치는 부분 제외
            if brown == 2 * a + 2 * (b - 2):
                return [a, b]

# test
print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))