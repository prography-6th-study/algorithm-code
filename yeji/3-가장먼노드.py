from collections import defaultdict, deque

def bfs(start, tables, visited):
    que = deque()
    que.append((start, 0))
    visited.add(start)

    numbers = defaultdict(lambda:0)

    while(que):
        node, cnt = que.popleft()
        visited.add(node)
        for n in tables[node]:
            if n not in visited:
                visited.add(n)
                numbers[cnt+1]+=1
                que.append((n, cnt+1))
    return numbers[cnt]

def solution(n, edge):
    tables = defaultdict(set)
    for a, b in edge:
        tables[a].add(b)
        tables[b].add(a)
    print(tables)
    visited = set()
    return bfs(1, tables, visited)

"""
풀이방법
1에 대해 bfs로 탐색하기
"""