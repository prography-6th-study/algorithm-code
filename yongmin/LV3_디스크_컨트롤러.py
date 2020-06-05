import heapq

def solution(jobs):
    jobs.sort()
    working_hours = 0  # 작업에 걸린 시간
    time = jobs[0][0]  # 경과 시간 초기화
    pq = []  # 작업 대기 중인 요청들을 담을 우선순위 큐
    cnt = 0  # 작업을 끝낸 요청 카운트

    while jobs:
        # jobs에서 첫 번째 값을 꺼내옴
        (request, cost) = jobs.pop(0)  # (요청시간, 소요시간)
        time += cost  # 경과시간에 소요시간을 더해줌
        cnt += 1  # 작업을 끝낸 요청 +1
        working_hours += (time - request)  # 작업에 걸린 시간 = 경과시간 - 요청시간

        # jobs가 비어있지 않고, jobs 첫번째 요소의 요청시간이 경과시간보다 작을 때
        while jobs and jobs[0][0] < time:
            (request, cost) = jobs.pop(0)  # jobs의 첫번째 요소를 꺼내
            heapq.heappush(pq, (-cost, request))  # pq에 저장 (최대힙으로)

        # pq에 원소가 있는 동안
        while pq:
            # pq에서 원소를 꺼내 jobs에 첫번째로 저장
            # cost의 최대값이 먼저 jobs 0번째에 들어가므로
            # jobs에는 cost의 최소값이 0번째에 있게 된다
            (cost, request) = heapq.heappop(pq)
            jobs.insert(0, [request, -cost])

    return working_hours // cnt  # 경과시간에 작업을 끝낸 요청 개수를 나눈 몫을 리턴

# test
print(solution([[0, 3], [1, 9], [2, 6]]))
