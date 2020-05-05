def dfs(computers, visited, v):
    if visited[v] == 0:
        visited[v] = 1
    for e in range(len(computers)):
        if computers[v][e] == 1 and visited[e] == 0:
            dfs(computers, visited, e)

def solution(n, computers):
    visited = [0] * n
    answer = 0
    while 0 in visited:
        for i in range(n):
            if visited[i] == 0:
                dfs(computers, visited, i)
                answer += 1
    return answer


# test
c1 = [[1, 1, 0],
      [1, 1, 0],
      [0, 0, 1]]
print(solution(3, c1))

c2 = [[1, 1, 0],
      [1, 1, 1],
      [0, 0, 1]]
print((solution(3, c2)))

# 문제가 어려워서 다른 사람의 풀이를 참고했다.
# 아직 이해하지 못했다.. LV3은 너무 어렵다..