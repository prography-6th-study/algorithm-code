def solution(N):
    # 타일 길이를 담을 리스트
    fibo = [0 for v in range(N+1)]
    fibo[0] = 1
    fibo[1] = 1

    # 타일 길이를 구한다
    for i in range(2, N+1):
        fibo[i] = fibo[i-1] + fibo[i-2]

    # 타일의 개수가 N일 때 구하려는 둘레는 2 * (N번째 타일 길이) + 2 * (N+1번째 타일 길이)
    return 2 * fibo[N-1] + 2 * fibo[N]



# test
print(solution(5))
print(solution(6))