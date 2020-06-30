def solution(n, costs):
    answer = 0
    # 비용을 기준으로 오름차순 정렬
    costs.sort(key=lambda cost: cost[2])
    visited = [0] * n  # 섬을 방문했는지 여부를 담을 리스트
    visited[0] = 1  # 첫번째 섬은 방문했다고 가정
    while sum(visited) != n:
        for current, next, cost in costs:
            # 두 섬 모두 이미 방문한 경우는 패스
            if visited[current] and visited[next]:
                continue
            # 모든 섬을 연결하기 위해
            # 두 섬 중에 하나는 방문한 경우만 visited를 갱신
            if visited[current] + visited[next] == 1:
                visited[current] = 1
                visited[next] = 1
                answer += cost
                break

    return answer


# test
print(solution(4, [[0,1,1], [0,2,2], [1,2,5], [1,3,1], [2,3,8]]))
print(solution(5, [[0,1,1],[0,2,2],[1,2,5],[1,3,3],[2,3,8],[3,4,1]]))

