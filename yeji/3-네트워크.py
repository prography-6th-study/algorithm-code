def solution(n, computers):
    visited = [0] * n
    answer = 0

    def search(computers, visited, startNode):
        stack = [startNode]
        while stack:
            i = stack.pop()
            if visited[i] == 0:
                visited[i] = 1
            for j in range(len(computers)):
                if computers[i][j] == 1 and visited[j] == 0:
                    stack.append(j)
    
    i = 0
    while 0 in visited:
        if visited[i] == 0:
            search(computers, visited, i)
            answer += 1
        i+=1
    return answer

"""
풀이방법
visited 배열을 컴퓨터 갯수만큼 만들어놓고 모두 방문할 때까지 탐색
연결된 컴퓨터 찾을 때 dfs 사용
"""