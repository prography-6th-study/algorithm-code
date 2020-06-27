"""
도저히 못 풀겠어서 찾아봤는데, 풀이도 python 1개, c++ 1개 밖에 없어서 c++로 풀어져있는 거 python으로 변환해봤습니다. 흐윽 ㅠㅠ
아래 풀이는 vertex(정점, node)를 방문했는지, edge(간선)을 방문했는지 둘 다 비교해가면서 
서로 다른 경로를 이용해 같은 정점으로 2번 들어오면 cycle이 생기는 것이므로, 해당 시점에 count를 증가시켜주는 풀이입니다.
X가 형태로 방이 생기는 경우는 아직 이해가 잘 안되네용.. 행아웃 전까지 고민해보겠씁니다...!
"""


def solution(arrows):
    cnt, vertex_visited, edge_visited = 0, dict(), dict()
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    x, y = 0, 0
    vertex_visited[(x, y)] = 1
    for i in range(len(arrows)):
        for j in range(2):  # X자의 교차 형태를 세기 위함
            nx = x + dx[arrows[i]]
            ny = y + dy[arrows[i]]
            if vertex_visited.get((nx, ny), 0) == 1:
                if edge_visited.get((x, y, nx, ny), 0) == 0:
                    cnt += 1
            vertex_visited[(nx, ny)] = 1
            edge_visited[(x, y, nx, ny)] = 1  # 정방향?
            edge_visited[(nx, ny, x, y)] = 1  # 역방향?
            x, y = nx, ny
    return cnt


a = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]

print(solution(a))
