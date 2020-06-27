"""
바위 사이의 거리를 이용하는 것은 알겠는데, 어떤 식으로 이분탐색을 적용해야 할지 몰라서 블로그 코드를 참고했다..
제거한 바위 개수가 testcase에서 주어진 값보다 큰지, 작은지를 이용해 이분탐색의 start와 end값을 갱신하는 거였다.
바위 사이의 거리를 찾는 값으로 두고 이분탐색으로 O(logN) 의 시간복잡도로 해당 값을 찾는 문제이다.
(rocks + 1) ==> 50001 가 바위의 최대 개수니까 순차탐색으로 가면 최대 50001번의 비교인 것에 비해
이분탐색을 쓰면 log(50001) = 15.6, 즉, 16번 이내의 비교를 거쳐서 효율적으로 target 값을 찾을 수 있는 것이라 이해했다.
"""


def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 0, distance
    ret = 0
    while left <= right:
        min_dist = float('inf')
        tmp = 0
        removed = 0
        mid = (left + right) // 2
        for i in range(len(rocks)):
            if rocks[i] - tmp < mid:  # 돌 사이의 거리 < 최소 거리로 예상하는 값
                removed += 1  # 최소값 중에 가장 큰 값을 찾아야하기 때문에, 해당 돌 삭제
            else:
                min_dist = min(min_dist, rocks[i] - tmp)  # 최소값 갱신
                tmp = rocks[i]
        if removed > n:  # 삭제한 값이 주어진 삭제 바위 수보다 클 때
            right = mid - 1
        else:
            ret = min_dist
            left = mid + 1
    return ret


d = 25
r = [2, 14, 11, 21, 17]
n = 2

print(solution(d, r, n))
