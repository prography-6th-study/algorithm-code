def solution(a):
    # a의 길이가 1, 2, 3 인 경우 : 다 살아남으므로 길이가 정답
    if len(a) in [1, 2, 3]:
        return len(a)

    min_arr = [[1000000001, 1000000001] for _ in range(len(a))]  # 최소값을 담을 리스트
    left, right = 1000000001, 1000000001  # 왼쪽 방향 최소값, 오른쪽 방향 최소값
    for i in range(len(a)):
        # 왼쪽 방향 최소값 구하기
        if a[i] < left:
            left = a[i]
        min_arr[i][0] = left
        # 오른쪽 방향 최소값 구하기
        if a[len(a) - (i + 1)] < right:
            right = a[len(a) - (i + 1)]
        min_arr[len(a) - (i + 1)][1] = right

    answer = 2  # 양 끝값은 무조건 살아남으므로 정답을 2로 초기화
    # 1부터 n - 1 까지
    for i in range(1, len(a) - 1):
        # 왼쪽 최소값과 오른쪽 최소값이 모두 a[i] 보다 작으면 a[i]는 살아남지 못함
        if min_arr[i][0] < a[i] and min_arr[i][1] < a[i]:
            continue
        answer += 1
    return answer


# test
print(solution([9, -1, -5]))
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))