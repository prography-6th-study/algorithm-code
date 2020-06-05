"""
heap을 이용해서 가장 짧은 요청부터 먼저 수행할 수 있게 함

"""


import heapq

def solution(jobs):
    answer = 0
    last, time, q = -1, 0, []
    cnt = 0
    n = len(jobs)
    while cnt < n:
        for job in jobs:
            if last < job[0] <= time:
                answer += time - job[0] # 현재 시간부터 작업이 들어온 시간을 빼서 더함
                heapq.heappush(q, job[1])
        if len(q) > 0:
            answer += len(q) * q[0] # 하나의 작업이 끝날 때까지 같이 기다리고 있는 작업 개수만큼 곱해서 더함
            last = time
            time += heapq.heappop(q)
            cnt += 1
        else:
            time += 1
    return answer // n


j = [[0, 3], [1, 9], [2, 6]]
print(solution(j))