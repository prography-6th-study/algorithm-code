import heapq
def solution(scoville, K):
    heap = []
    result = 0
    number = 0
    for item in scoville:
        heapq.heappush(heap, item)
    while(True):
        first = heapq.heappop(heap)
        if first >= K:
            return number
        if len(heap) == 0:
            return -1
        second = heapq.heappop(heap)
        result = first + second*2
        heapq.heappush(heap ,result)
        number +=1
