def solution(n, times):
    left = 1
    right = max(times) * n
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        count = [mid // t for t in times]
        if sum(count) >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


"""
[ 풀이방법 ]
    - 중간값을 총 시간으로 두고, 그 안에서 times가 총 몇명을 심사할 수 있는지 확인한다.
    - 총 심사 가능한 인원이 n 보다 커지는 경우를 업데이트 해주면서 가장 작은 값을 찾아간다.
"""
