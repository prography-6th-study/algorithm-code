def dfs(m, n, a):
    global cnt, flag
    li = []
    d = dict()
    for i in range(m - 1):
        for j in range(n - 1):
            if a[i][j] == '0': # 비어 있는 칸이면 pass
                continue
            if a[i][j] == a[i + 1][j] == a[i][j + 1] == a[i + 1][j + 1]: # 2 x 2 블록의 모양이 모두 같다면
                li += [(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)]
    if not li: # 같은 블록이 하나도 존재하지 않는다면 재귀함수 탈출
        flag = True
        return
    s = set(li)
    cnt += len(s)
    for ele in s:
        d[ele[1]] = d.get(ele[1], []) + [ele[0]] # 열 별로 사라지는 블록의 index를 넣어둠

    tmp_a = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            tmp_a[j][i] = a[i][j]  # 행-열을 열-행 배열로 전환 

    tmp = [i for i in range(m)]
    # 같은 블록 지우고 떨어뜨리기
    for k in d: 
        ret = ""
        ts = "".join(tmp_a[k])
        remain = set(tmp) - set(d[k])
        for r in remain:
            ret += ts[r]
        tcnt = len(tmp) - len(ret)
        ret = '0' * tcnt + ret
        tmp_a[k] = list(ret)

    for i in range(m):
        for j in range(n):
            a[i][j] = tmp_a[j][i]
    if not flag:
        dfs(m, n, a)

cnt = 0
flag = False
def solution(m, n, board):
    a = [list(i) for i in board]
    dfs(m, n, a)
    return cnt

print(solution(6, 2, ["AA", "AA", "CC", "AA", "AA", "DD"]))
print(solution(6, 2, ["DD", "CC", "AA", "AA", "CC", "DD"]))
print(solution(3, 2, ['AA', 'AA', 'AB']))
print(solution(2, 2, ['AA', 'AB']))
print(solution(4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))
print(solution(6, 6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']))