"""
dfs를 이용해서 구현
visited 배열을 컴퓨터 개수만큼 만들어놓고, visited 값이 모두 방문했음(1)으로 바뀔 때까지
연결된 모든 컴퓨터를 방문하며 visited 값을 1로 바꾸는 함수 dfs를 재귀 호출.
"""

def dfs(x, computers, visited):
    if visited[x] == 1:
        return
    visited[x] = 1
    for nx in range(len(computers)):
        if not visited[nx] and computers[x][nx] == 1: # 연결은 되어있는데, 방문을 안했을 경우
            dfs(nx, computers, visited)


def solution(n, computers):
    cnt = 0
    visited = [0] * (n)
    while not set(visited) == {1}:
        dfs(visited.index(0), computers, visited)
        cnt += 1
    return cnt