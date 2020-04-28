import heapq

def solution(stock, dates, supplies, k):
    cnt = 0
    idx = 0  # 시작점
    h = []

    while stock < k:  # stock이 k 이상일 때까지 반복
        # 시작점부터 dates의 끝까지 반복
        for i in range(idx, len(dates)):
            if stock < dates[i]: break  # stock dates[i]보다 작으면 반복을 멈춘다
            heapq.heappush(h, -supplies[i])   # 최대 힙으로 데이터 저장
            idx = i + 1   # 시작점을 i+1로 변경

        stock += heapq.heappop(h) * (-1)  # 반복문 빠져나오면 힙에서 데이터를 꺼내 stock에 더해준다
        cnt += 1   # 공급횟수 증가

    return cnt

# test
stock = 6
dates = [4, 10, 15]
supplies = [20, 5, 10]
k = 30
print(solution(4, dates, supplies, k))