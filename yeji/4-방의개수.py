from collections import deque

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def solution(arrows):
    cnt, dir, q = {}, {}, deque()
    cnt[(0, 0)] = 0
    q.append([0, 0])
    x, y, ans = 0, 0, 0

    for i in arrows:
        for j in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            cnt[(nx, ny)] = 0
            dir[(x, y, nx, ny)] = 0
            dir[(nx, ny, x, y)] = 0
            q.append([nx, ny])
            x, y = nx, ny

    x, y = q.popleft()
    cnt[(x, y)] = 1
    while q:
        nx, ny = q.popleft()

        if cnt[(nx, ny)] == 1:
            if dir[(x, y, nx, ny)] == 0:
                ans += 1
                dir[(x, y, nx, ny)] = 1
                dir[(nx, ny, x, y)] = 1
        else:
            cnt[(nx, ny)] = 1
            dir[(x, y, nx, ny)] = 1
            dir[(nx, ny, x, y)] = 1
            
        x, y = nx, ny

    return ans

"""풀이방법

방이 만들어졌는지 어떻게 확인할지를 한참 고민하다가 결국 포기했당 
느므 어렵다 이거 누가 풀어 진짜

1. 방문한 좌표와 이동경로를 key로 하는 dict를 2개 만들고 방문하면 1로 저장한다
2. 왔던 경로를 반대로 돌아가는 경로를 고려하여 경로를 저장하는 dir에 반대방향으로 이동하는 경로도 체크
3. X 자로 교차하여 방을 만드는 경우를 고려하여 한번 이동할때 2칸씩 이동
  이렇게 하면 X자로 교차되는 지점의 좌표를 지정할 수 있다
4. 다음 좌표가 이전에 방문한 적이 있고 이동한 적 없는 경로라면 방을 만들게 되므로 방의 개수를 증가
5. 그 외의 경우에는 좌표를 방문했음을 체크하고 경로도 체크
"""