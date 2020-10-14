from itertools import combinations

def solution(numbers):
    comb = list(combinations(numbers, 2))  # 2개를 뽑은 조합 구하기
    result = [sum(x) for x in comb]  # 2개를 더한 값으로 리스트 만들기
    return sorted(list(set(result)))  # 셋으로 변환해서 중복값 제거 -> list -> 정렬


# test
print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
print(solution([100, 100, 100]))