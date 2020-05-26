import operator

def solution(progresses, speeds):
    answer = []

    # 큐(progresses)에 있는 동안 반복
    while progresses:
        # 하루가 지나면 진행률에 speed 만큼 더해줌
        progresses = list(map(operator.add, progresses, speeds))

        count = 0
        # 큐의 첫번째 원소가 100보다 크면 하나씩 pop하면서 개수를 센다
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1

        # count가 0보다 크면 answer에 추가
        if count > 0:
            answer.append(count)

    return answer


# test
print(solution([93, 30, 55], [1, 30, 5]))