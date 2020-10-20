def solution(n):
    # 1, 2 인 경우 뒤집고 10진법해도 같은 값
    if n in [1, 2]:
        return n

    arr = []
    while n:
        n, r = divmod(n, 3)  # 몫, 나머지
        arr.append(r)  # 나머지 추가
        # n이 3보다 작으면 n을 추가하고 종료
        if n < 3:
            arr.append(n)
            break

    m = len(arr) - 1  # m 제곱
    answer = 0
    for v in arr:
        answer += v * (3 ** m)
        m -= 1

    return answer


# test
print(solution(45))
print(solution(125))