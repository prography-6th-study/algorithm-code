import heapq

def solution(stock, dates, supplies, k):
    cnt = 0
    idx = 0
    h = []

    while stock < k:
        for i in range(idx, len(dates)):
            if stock < dates[i]: break
            heapq.heappush(h, -supplies[i])
            idx += 1

        stock += heapq.heappop(h) * (-1)
        cnt += 1

    return cnt

#test
stock = 4
dates = [4, 10, 15]
supplies = [20, 5, 10]
k = 30
print(solution(4, dates, supplies, k))