def solution(n):
    answer = 0
    # n이 0이 될 때까지 반복 (n에서 0으로 간다고 생각)
    while n > 0:
        # n이 홀수이면 한칸 점프
        if n % 2 == 1:
            answer += 1
            n -= 1
        n = n // 2  # n을 2로 나눈다
    return answer

# 순간이동 (*2)를 최대로 사용해야 답을 구할 수 있는 문제
# 0 -> n 으로 가는 것을 n -> 0 생각하면
# 점프는 n에서 빼주고 순간이동은 n에서 2로 나눠준다
# 순간이동을 최대로 사용하기 위해 점프는 1칸만..


# test
print(solution(5))
print(solution(6))
print(solution(5000))