# 가장 먼 노드
def solution(n, edge):
    # 초기화
    graph = [[] for _ in range(n)]
    distances = [0] * n
    is_visited = [False for _ in range(n)]

    # 시작 노드 방문
    queue = [0]
    is_visited[0] = True

    # 노드 연결
    for (a, b) in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    # 거리 계산
    while queue:
        current = queue.pop(0)
        # 현재 노드에서 갈 수 있는 노드들을 반복문을 돌며 방문 처리
        for adjacent in graph[current]:
            # 방문하지 않은 노드라면 큐에 추가하고,
            # 인접노드의 거리 : 1부터 현재노드까지의 거리 +1
            if is_visited[adjacent] == False:
                is_visited[adjacent] = True
                queue.append(adjacent)
                distances[adjacent] = distances[current] + 1

    # 거리가 최대인 것들을 카운트
    return distances.count(max(distances))


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))