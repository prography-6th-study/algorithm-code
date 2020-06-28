def solution(n, costs):
  costs.sort(key=lambda x: x[2]) # 가중치가 낮을 수록 앞으로 간다
  visited = [0] * n
  answer = 0
  visited[0] = 1

  while sum(visited) != n :
    for c in costs:
      start, end, cost = c
      if visited[start] or visited[end]: # 둘 중 하나가 시작점
        if visited[start] and visited[end]: # 이미 연결된 길이라 패스
          continue
        else:
          #if 로 start가 1일 때와 end가 1일 때 나누기 귀찮아서 그냥 둘 다 해버림 
          visited[start] = 1 
          visited[end] = 1
          # 비용 증가
          answer += cost
          break

  return answer