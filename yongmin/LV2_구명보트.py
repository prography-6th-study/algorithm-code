def solution(people, limit):
    # people을 정렬한 후 가장 가벼운 사람과 무거운 사람의 무게를 합하여 limit와 비교하고
    # 2명이서 같이 나갈지, 무거운 사람만 나갈지 판단

    people.sort(reverse=True)  # people을 내림차순으로 정렬
    start, end = 0, len(people) - 1  # 시작점, 끝점

    # 시작점이 끝점보다 커질 때까지
    while start <= end:
        # 남아있는 가장 무거운 사람 무게 + 가장 가벼운 사람 무게 <= limit : 같이 탈출
        # 그게 아니면 가장 무거운 사람만 혼자 탈출
        if people[start] + people[end] <= limit:
            end -= 1  # 가장 가벼운 사람을 같이 탈출시킨다
        start += 1  # 가장 무거운 사람을 탈출시킨다
    # start 값이 사람들이 나간 횟수
    return start


# test
print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))