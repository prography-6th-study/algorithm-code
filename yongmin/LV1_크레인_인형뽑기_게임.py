def solution(board, moves):
    stack = []
    answer = 0

    # 칼럼별로 인형 정리
    cols = {}
    for b in board:
        for i in range(len(b)):
            if b[i] == 0:
                continue
            try:
                cols[i+1].insert(0, b[i])
            except KeyError:
                cols[i+1] = [b[i]]
    # {3: [1, 4, 5, 1], 5: [1, 2, 1, 3], 2: [5, 2, 2], 1: [3, 4], 4: [3, 4]}

    for m in moves:
        # 해당 열에 인형 없으면 패스
        if len(cols[m]) == 0:
            continue

        current = cols[m].pop()  # 인형 뽑기
        # 스택이 비어 있다면 스택에 추가
        if len(stack) == 0:
            stack.append(current)
            continue
        # 스택 마지막 값과 현재 뽑은 인형 값이 같으면
        if current == stack[-1]:
            stack.pop()  # 스택에서 인형 제거
            answer += 2  # 인형 2개가 터짐
        # 다르면 스택에 인형 추가
        else:
            stack.append(current)

    return answer

# test
print(solution([[0, 0, 0, 0, 0],
                [0, 0, 1, 0, 3],
                [0, 2, 5, 0, 1],
                [4, 2, 4, 4, 2],
                [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))