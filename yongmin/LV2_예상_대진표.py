def solution(n, a, b):
    answer = 0  # 라운드를 카운트
    while True:
        answer += 1
        # a, b가 홀수일 경우
        if a % 2 == 1:
            a += 1
        if b % 2 == 1:
            b += 1
        # 다음 라운드의 번호는 나누기 2 한 값
        a, b = a // 2, b // 2
        # a, b의 번호가 같아지는 시점에서 서로 붙는다
        if a == b:
            break
    return answer


# test
print(solution(8, 4, 7))