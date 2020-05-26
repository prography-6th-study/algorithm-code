def solution(clothes):
    # 딕셔너리로 변환
    d = {}
    for cloth in clothes:
        try:
            d[cloth[1]].append(cloth[0])
        except KeyError:
            d[cloth[1]] = [cloth[0]]

    # 경우의 수 :
    # 각 카테고리의 개수 + 1 을 곱한 후 1을 빼준다
    # (a + 1) * (b + 1) * (c + 1) *... - 1
    # +1 은 해당 카테고리가 선택되지 않은 경우
    # -1 은 모든 카테고리에서 선택되지 않은 경우를 제외하기 위한 것
    answer = 1
    for key in list(d.keys()):
        answer *= len(d[key]) + 1

    answer = answer - 1

    return answer


# test
print(solution([["yellow_hat", "headgear"],
                 ["blue_sunglasses", "eyewear"],
                 ["green_turban", "headgear"]]))

print(solution([["crow_mask", "face"],
                ["blue_sunglasses", "face"],
                ["smoky_makeup", "face"]]))