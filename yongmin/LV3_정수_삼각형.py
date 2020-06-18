def solution(triangle):
    # 정답을 담을 리스트 초기화
    answers = triangle.pop()

    # 트라이앵글에 원소가 있을 때 까지 반복
    while(triangle):
        # 트라이앵글을 밑에서부터 한 줄 pop
        row = triangle.pop()
        temp = []
        # row 길이만큼 반복
        for i in range(len(row)):
            # answers가 밑에 줄, row가 위에 줄
            # 밑에 줄에서 위에 줄로 가는 경로는 row 각 요소마다 2개씩
            # row 각 요소에 가는 경로 2가지 중 최대값을 저장
            temp.append(max(row[i] + answers[i], row[i] + answers[i+1]))
        answers = temp  # 결과를 answers로
    return answers[0]


# test
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))