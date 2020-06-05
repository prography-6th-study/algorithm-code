import heapq

def solution(jobs):
  n = len(jobs)
  time, end, que = 0, -1, []
  count = 0 #처리한 프로세스 수
  answer = 0

  while count < n:
    for i in jobs:
      if end < i[0] <= time:
        # 현재시간 기준 프로세스가 que에서 얼마나 기다렸는지
        answer += (time - i[0])
        heapq.heappush(que, i[1])
      
    if len(que) > 0:
      # 가장 빨리 끝나는 프로세스가 끝날 때까진 대기시간이니까 추가
      answer += len(que) * que[0]
      # 끝난 시간
      end = time
      # 가장 빨리 끝난 프로세스가 걸린 시간 더해줌
      time += heapq.heappop(que)
      # 프로세스가 끝났으니까 count+1
      count += 1
    else:
      # que에 아직 아무것도 없음
      time += 1
  return answer//n