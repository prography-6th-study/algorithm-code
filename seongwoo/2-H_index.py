def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        print( l, i)
        if citations[i] >= l - i: # 인용된 횟수 >= 인용된 논문 개수
            return l - i
    return 0

c = [3, 0, 6, 1, 5]
print(solution(c))