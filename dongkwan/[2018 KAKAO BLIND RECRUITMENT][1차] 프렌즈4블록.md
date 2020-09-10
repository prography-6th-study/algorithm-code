문제 설명
프렌즈4블록
블라인드 공채를 통과한 신입 사원 라이언은 신규 게임 개발 업무를 맡게 되었다. 이번에 출시할 게임 제목은 프렌즈4블록.
같은 모양의 카카오프렌즈 블록이 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.

board map
만약 판이 위와 같이 주어질 경우, 라이언이 2×2로 배치된 7개 블록과 콘이 2×2로 배치된 4개 블록이 지워진다. 같은 블록은 여러 2×2에 포함될 수 있으며, 지워지는 조건에 만족하는 2×2 모양이 여러 개 있다면 한꺼번에 지워진다.

board map

블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 된다.

board map

만약 빈 공간을 채운 후에 다시 2×2 형태로 같은 모양의 블록이 모이면 다시 지워지고 떨어지고를 반복하게 된다.
board map

위 초기 배치를 문자로 표시하면 아래와 같다.

TTTANT
RRFACC
RRRFCC
TRRRAA
TTMMMF
TMMTTJ
각 문자는 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)을 의미한다

입력으로 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작하라.

입력 형식
입력으로 판의 높이 m, 폭 n과 판의 배치 정보 board가 들어온다.
2 ≦ n, m ≦ 30
board는 길이 n인 문자열 m개의 배열로 주어진다. 블록을 나타내는 문자는 대문자 A에서 Z가 사용된다.
출력 형식
입력으로 주어진 판 정보를 가지고 몇 개의 블록이 지워질지 출력하라.

입출력 예제
m	n	board	answer
4	5	[CCBDE, AAADE, AAABF, CCBBF]	14
6	6	[TTTANT, RRFACC, RRRFCC, TRRRAA, TTMMMF, TMMTTJ]	15
예제에 대한 설명
입출력 예제 1의 경우, 첫 번째에는 A 블록 6개가 지워지고, 두 번째에는 B 블록 4개와 C 블록 4개가 지워져, 모두 14개의 블록이 지워진다.
입출력 예제 2는 본문 설명에 있는 그림을 옮긴 것이다. 11개와 4개의 블록이 차례로 지워지며, 모두 15개의 블록이 지워진다.
해설 보러가기



### 코드


```python
# 정, 우, 하, 대하
dx = [0,1,0,1]
dy = [0,0,1,1]

def safe(width,height,c_idx,r_idx):
    for x,y in zip(dx,dy):  # 4번 돈다.
        if x+c_idx>width-1 or x+c_idx<0 or y+r_idx>height-1 or y+r_idx<0:
            return False
    return True

def del_check(board,c_idx,r_idx):
    square_set = set()
    for x,y in zip(dx,dy):
        square_set.add(board[r_idx+y][c_idx+x])
    if len(square_set)==1 and square_set != {" "}:
        return True
    return False

def del_block(board,c_idx,r_idx):
    for x,y in zip(dx,dy):
        board[y+r_idx][x+c_idx]=""
    return board

def drop_block(width,height,board):
    for x_idx in range(width):
        tmp_list = []
        for y_idx in range(height):
            tmp_list.append(board[y_idx][x_idx]) # 세로 위에서 아래로 더해줌
        col_str = "".join(tmp_list)
        col_str = (height-len(col_str))*" " + col_str
        col_str = [block for block in col_str]
        for y_idx in range(height):
            board[y_idx][x_idx] = col_str[y_idx]    # 재분배
    return board

def total_del_block(board):
    answer = 0
    for row in board:
        for block in row:
            if block==" ":
                answer += 1
    return answer

def solution(height,width,board):
    board = [[block for block in row] for row in board]
    while True:
        del_list = []
        for r_idx in range(height):
            for c_idx in range(width):
                if safe(width,height,c_idx,r_idx):
                    if del_check(board,c_idx,r_idx):
                        del_list.append([c_idx,r_idx])  # 후보군 리스트에 담는다.
        if len(del_list)==0:
            break
        for del_pos in del_list:
            board = del_block(board,del_pos[0],del_pos[1])  # 한방에 다 터뜨린다.
        board = drop_block(width,height,board)
    count = total_del_block(board)

    return count
```

