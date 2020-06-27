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


# test
print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))


# 너무 어려워서 블로그에서 다른 사람의 풀이를 참고했지만 아직 모르겠다..