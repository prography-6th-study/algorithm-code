def solution(prices):
    answer = []

    for i in range(len(prices)):
        cnt = 0  # 가격이 떨어지지 않은 기간
        for j in range(i+1, len(prices)):
            cnt += 1
            # 기준값 > 기준값 뒤의 가격 : 가격이 떨어짐
            if prices[i] > prices[j]:
                break
        answer.append(cnt)

    return answer


# test
print(solution([1, 2, 3, 2, 3]))