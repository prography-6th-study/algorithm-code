"""
풀면서 zip(*iterable)의 용법을 공부했다. *(asterisk)는 파라미터의 개수를 몇 개 받을지 모를 때 사용함. (ex> *args)
for문이 많이 얽혀서 그런지 기본 테스트케이스와 나머지 테스트케이스 1/4만 통과하고 나머지는 시간초과로 인해 실패

결국 다른 사람 풀이보고 풀었는데, set의 discard() 함수를 알게 되었다.
set은 element를 지우기 위해서 remove(), discard() 두 개의 함수를 가지고 있다.

- remove() : 지우려는 element가 set에 없으면 KeyError 발생
- discard() : 지우려는 element가 없어도 오류 발생 없이 종료
"""

from itertools import combinations

def solution_mine(relation):
    l = len(relation[0])
    cnt = 0
    li= [[] for _ in range(l)]
    for r in relation:
        for i in range(len(r)):
            li[i].append(r[i])
    for idx, each_li in enumerate(li):
        if len(set(each_li)) == len(each_li):
            cnt += 1
            li.pop(idx)
    for n in range(2, len(li) + 1):
        for comb in list(combinations([i for i in range(len(li))], n)):
            temp = []
            for c in comb:
                temp.append(li[c])
            s = sorted(list(set(zip(*temp))))
            original = sorted(list(zip(*temp)))
            if s == original:
                cnt += 1
                for i in comb:
                    li.pop(i)
            if len(li) == 1:
                return cnt
    return cnt

def solution(relation):
    c_li = []
    unique = []
    l = len(relation[0])
    for i in range(1, l + 1):
        c = combinations([i for i in range(0, l)], i)
        c_li.extend(c)

    # 유일성 (구별할 수 있는 조합)
    for comb in c_li:
        temp = []
        for row in range(0, len(relation)):
            temp_li = [relation[row][i] for i in comb]
            temp.append(tuple(temp_li))
        if len(set(temp)) == len(relation):
            unique.append(comb)

    # 최소성
    s = set(unique)
    for i in range(0, len(unique) - 1): # 후보키의 갯수가 작은 것부터 확인하므로
        for j in range(i + 1, len(unique)):
            if set(unique[i]) == set(unique[i]) & set(unique[j]): # 나머지 현재 인덱스 이후로 겹치는 것이 있다면 최소성을 만족하지 않으므로
                s.discard(unique[j]) # 삭제

    return len(s)


r = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]

print(solution(r))