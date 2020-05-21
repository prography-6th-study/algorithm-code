"""
가장 오래걸리는 심사관 (n * 걸리는 시간) 기준으로 시작해서
mid를 한 심사관에게 걸리는 시간으로 두고,
최솟값이 되는 mid 값을 이분탐색으로 도출
"""

def solution(n, times):
    left, right = 1, max(times) * n
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for i in times:
            people += mid // i
            if people >= n:
                break
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

n = 6
times = [7, 10]

print(solution(n, times))