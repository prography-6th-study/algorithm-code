def solution(tickets):
    # 그래프 생성
    graph = dict()

    # 'start':[end, end]
    for (start, end) in tickets:
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]

    # 알파벳 순서상 맨 앞 값을 먼저 꺼내오기 위해 value 값을 역순으로 정렬
    for key in graph.keys():
        graph[key].sort(reverse=True)

    stack = ["ICN"]
    path = []

    while stack:
        top = stack[-1]

        # top이 graph에 없음 or top을 시작으로 하는 티켓이 없음
        if top not in graph or len(graph[top]) == 0:
            path.append(stack.pop())  # path에 저장
        # top을 시작점으로 하는 end 값 중 마지막 값을 빼서 stack에 저장
        else:
            stack.append(graph[top][-1])
            graph[top] = graph[top][:-1]

    return path[::-1]


# test
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
