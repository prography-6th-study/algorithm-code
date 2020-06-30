def solution(weight):
    weight.sort()  # 1 1 2 3 6 7 30
    # 무게 리스트의 누적합
    weight_sum = weight.pop(0)
    for w in weight:
        # 현재 추가 (누적합+1) 보다 크다면
        # (누적합+1)부터 현재 추 사이의 값을 만들 수 없다
        if w > weight_sum + 1:
            break
        else:
            weight_sum += w
    # 최소값을 리턴해야 하므로 누적합+1 리턴
    return weight_sum + 1


# test
print(solution([3, 1, 6, 2, 7, 30, 1]))