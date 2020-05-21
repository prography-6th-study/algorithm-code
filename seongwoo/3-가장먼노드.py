"""
bfs 이용해서 구현.
노드끼리 연결된 관계를 for문을 돌면서 graph 이중배열 안에 넣음.
이후 연결되어 있는 것 중 방문하지 않은 관계들에 대해 거리를 1씩 더하며, 각 노드들이 시작점으로 부터 떨어진 거리를 계산.
같은 거리에 있는 것들의 숫자를 반환.
"""

def solution(n, edge):
    graph = [[] for _ in range(n)]
    distances = [0 for _ in range(n)]
    is_visited = [False for _ in range(n)]

    queue = [0]
    is_visited[0] = True

    for (a,b) in edge:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    
    while queue:
        i = queue.pop(0)
        for j in graph[i]:
            if is_visited[j] == False:
                is_visited[j] = True
                queue.append(j)
                distances[j] = distances[i] + 1
    answer = distances.count(max(distances))
    return answer
    
n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n,edge))