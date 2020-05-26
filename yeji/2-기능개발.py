def solution(progresses, speeds):
    answer = []
    N = len(progresses)
    p = 0
    while N!=p:
        tmp = 0
        for i in range(p, N):
            progresses[i] += speeds[i]
        if progresses[p] >= 100:
            for i in range(p, N):
                if progresses[i] >= 100:
                    tmp += 1
                    
                else:
                    break
            answer.append(tmp)
            p += tmp
    return answer

"""풀이방법
progress에 speed를 차례차례 더한다
p(현재 진행)이 100이상이면 progress에서 빼주고 answer에 더함
p를 진행완료된 지점까지 이동
"""