import math
def solution(distance,rocks, n):
    answer = 0
    start, end = 0, distance
    rocks = sorted(rocks)
    rocks.append(distance)
    rnum = len(rocks)
 
    while(start <= end):
        remove = 0
        prev = 0
        min_inter = math.inf # 무한대
        mid = (start + end)//2
 
        for i in range(rnum):
            if rocks[i]-prev < mid:  #rocks[i]-prev가 inter값
                remove += 1 #바위제거
                
            else: #바위 제거 안할경우 
                min_inter = min(min_inter,rocks[i]-prev) #inter값 갱신.
                prev = rocks[i] #현재 바위위치를 prev로
 
        #너무 많이 제거되었을 경우, 기준을 높여서 제거를 줄여야함
        if remove > n:
            end = mid-1
        #적게 제거되었을 경우, 기준을 낮춰서 제거를 늘려야함
        else:
            answer = min_inter
            start = mid+1
            
    return answer

"""풀이방법
탐색 기준: 돌과 돌 사이의 거리
진행 방법
1. 돌과 돌 사이의 거리가 이분탐색 기준값 보다 작은 경우 뒤쪽 돌 삭제
2. 삭제한 돌 갯수가 기준 n 보다 클 경우 돌과 돌 사이 거리를 줄이고 n보다 작거나 같으면 늘림

풀이 열심히 읽어봤지만 왜 이렇게 푸는지 아직도 이해가 잘 안간다......ㅠㅠ
"""
