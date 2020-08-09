def solution(N, stages):
    rates = {}  # stage: rate
    reached = len(stages)  # 도달한 사람들 count

    # 1번 스테이지부터 N번까지 돌면서
    for stage in range(1, N+1):
        # 도달한 사람이 있으면 실패율 계산
        if reached != 0:
            current = stages.count(stage)  # 스테이지에 도달했지만 클리어하지 못한 사람들 count
            rates[stage] = current / reached  # 실패율 계산
            reached -= current  # 현재 스테이지에 있는 사람들은 다음 스테이지에 도달하지 못하므로 빼준다
        else:
            rates[stage] = 0

    return sorted(rates, key=lambda x : rates[x], reverse=True)


# test
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))