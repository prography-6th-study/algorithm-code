"""
테스트케이스 moves 배열을 보면 1이 3번 나오는데
실제 1칸에 보면 인형이 2개 밖에 들어있지 않아 이에 대한 처리를 해줘야됐는데
처음에 하지 않아서 계속 테스크케이스 1,2번이 실패가 떴었다. 이 처리를 한 후에 통과하였다.
"""

def solution(board, moves):
    s = []
    cnt = 0
    for m in moves:
        doll = None
        for i in board:
            if i[m - 1] != 0:
                doll = i[m - 1]
                i[m - 1] = 0
                break
        if doll == None:
            continue
        if s != []:
            if s[-1] != doll:
                s.append(doll)
            else:
                s.pop()
                cnt += 2
        else:
            s.append(doll)
    return cnt

b = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
m = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(b,m))