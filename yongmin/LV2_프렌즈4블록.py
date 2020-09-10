def remove_character(cols, n):
    # 방문 처리
    temp = [[] for _ in range(n)]
    for i in range(len(cols) - 1):
        for j in range(len(cols[i]) - 1):
            try:
                # 현재 블록(왼쪽 위)을 기준으로 오른쪽 위, 왼쪽 아래, 오른쪽 아래 블록을 확인해서 모두 같으면 방문 처리
                if cols[i][j][0] == cols[i][j+1][0] and cols[i][j][0] == cols[i+1][j][0] and cols[i][j][0] == cols[i+1][j+1][0]:
                    cols[i][j][1] = 1
                    cols[i][j+1][1] = 1
                    cols[i+1][j][1] = 1
                    cols[i+1][j+1][1] = 1
            except IndexError:
                continue
    # 방문 횟수 세고 방문한 블록들 제거
    cnt = 0
    for i in range(len(cols)):
        for j in range(len(cols[i])):
            # 방문하지 않은 블록만 temp에 넣어줌
            if cols[i][j][1] == 0:
                temp[i].append(cols[i][j])
            # 방문한 경우 방문횟수 +1
            else:
                cnt += 1
    return temp, cnt


def solution(m, n, board):
    # 칼럼 별로 보드판 초기화
    cols = [[] for _ in range(n)]
    while board:
        b = board.pop()
        for i in range(n):
            cols[i].append([b[i], 0])  # [블록, 방문여부]
    answer = 0
    while True:
        cols, cnt = remove_character(cols, n)
        if cnt == 0:  # 더 이상 제거할 블록이 없는 경우
            break
        answer += cnt
    return answer


# test
print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))