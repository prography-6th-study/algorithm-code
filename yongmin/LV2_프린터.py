def solution(priorities, location):
    q = []
    # 초기화 : (인덱스, 우선순위)
    for i in range(len(priorities)):
        q.append((i, priorities[i]))

    answer = 0
    while q:    # 큐가 있는 동안 반복
        (i, p) = q.pop(0)

        # pop한 이후 큐에 원소가 없는 경우 :
        if len(q) == 0:
            answer += 1
            break

        # pop한 요소의 우선순위 값이 남은 것들 보다 크거나 같고
        if p >= max([ v[1] for v in q ]):
            answer += 1
            # 인덱스 값이 찾으려는 값이면 빠져나간다
            if i == location:
                break
        # 우선순위에 밀려 나갈 수 없으므로 마지막에 다시 값 추가
        else:
            q.append((i, p))

    return answer


# test
print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))