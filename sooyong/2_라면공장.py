import heapq


def solution(stock, dates, supplies, k) :
    ans = 0
    start = 0
    q = []
    while stock < k :
        for i in range(start, len(dates)) :
            if dates[i] <= stock :
                heapq.heappush(q, -supplies[i])
            else :
                start = i
                break
        ans += 1
        stock += -heapq.heappop(q)
    return ans
