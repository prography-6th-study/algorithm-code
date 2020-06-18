from collections import defaultdict

def solution(tickets):
  answer = []
  tmp = ["ICN"]
  graph = defaultdict(lambda:[])
  
  # 연결된 노드 정보 딕셔너리에 저장
  for start, end in tickets:
    graph[start].append(end)

  #인터넷 참고
  for g in graph:
    graph[g].sort(reverse=True)
  
  while tmp:
    current = tmp[-1]

    if current not in graph or len(graph[current]) == 0:
      answer.append(tmp.pop())
    else:
      tmp.append(graph[current].pop())

  answer.reverse()
  return answer

"""풀이방법
처음에는 그냥 그래프 만들어서 dfs하면 되긋네 했는데 알파벳 순이 안됐다
그래서 sort()를 하고 pop(0)를 했더니 또 안됐다
결국 한참 고민하다 인터넷을 뒤졌더니 reverse를 하더라
사람들은 똑똑하다..
"""