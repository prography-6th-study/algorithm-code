import heapq
def solution(stock, dates, supplies, k):
    answer = 0
    index = 0
    h = []

    while(stock < k):
        for i in range(index, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(h,(-supplies[i], supplies[i]))
                index += 1
            else:
                break
        stock += heapq.heappop(h)[1]
        answer += 1
    return answer

"""풀이방법
1. 최대 힙 기반의 우선순위 큐를 생성
2. stock이 k보다 작을 때까지
   - 만약 stock < dates[i]라면, 반복을 stop
   - 그 외에는 우선순위 큐에 supplies[i]를 넣음
   - idx를 i 바로 다음 인덱스로 옮김
3. 우선순위 큐에서 데이터를 꺼내 stock에 더함
4. answer에 1 더함
"""