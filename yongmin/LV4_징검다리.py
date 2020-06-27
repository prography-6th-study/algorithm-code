import math

def solution(distance, rocks, n):
    rocks.sort()  # 바위들의 위치 정렬
    rocks.append(distance)
    left, right = 0, distance
    answer = 0
    while left <= right:
        prev = 0  # 이전 돌
        mins = math.inf  # 거리의 최소값
        cnt = 0  # 제거한 돌의 개수

        mid = (left + right) // 2  # 돌과 돌 사이의 최소 거리 (기준값)
        for i in range(len(rocks)):
            # 돌과 돌 사이의 최소 거리보다 작을 경우 돌 삭제
            if rocks[i] - prev < mid:
                cnt += 1
            # 돌과 돌 사이의 최소 거리보다 클 경우 최소값을 구한다
            else:
                mins = min(mins, rocks[i] - prev)
                prev = rocks[i]

        # 제거한 돌의 개수가 n보다 크면 바위 제거를 줄여야 함
        # 돌과 돌 사이의 최소 거리를 작게 한다
        if cnt > n:
            right = mid - 1
        # 제거한 돌의 개수가 n보다 작으면 더 많은 바위를 제거해야 함
        # 돌과 돌 사이의 최소 거리를 크게 한다
        else :
            answer = mins
            left = mid + 1

    return answer


# test
print(solution(25, [2, 14, 11, 21, 17], 2))


# 너무 어려워서 블로그에서 다른 사람의 풀이를 참고했다.
# 이분탐색의 기준값을 저렇게 잡은 것은 이해가 가지만 이 값을 찾아나가는 과정은 아직 이해가 되지 않는다...
