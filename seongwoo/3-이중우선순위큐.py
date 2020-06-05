import heapq

def solution(operations):
    q = []
    for ele in operations:
        i, j = ele.split()
        if i == 'I':
            heapq.heappush(q, int(j))
        else:
            if i == 'D' and len(q) == 0:
                continue
            if j == '1':
                q.remove(max(q))
            else:
                heapq.heappop(q)
    if len(q) == 0:
        return [0, 0]
    return [max(q), min(q)]
    
ops = ["I 16", "D 1"]
print(solution(ops))