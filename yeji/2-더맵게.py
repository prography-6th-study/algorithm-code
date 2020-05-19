import heapq

def solution(scoville, K):
    turns = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        try:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            new = first + second*2
            heapq.heappush(scoville,new)
            turns += 1
        except IndexError:
            return -1

    return turns

"""풀이방법
scoville을 최소 힙으로 만들어줌
heappop으로 root(가장 작은 수)를 빼서 정해진 방식으로 계산
root가 k보다 커질 때까지 반복
"""
