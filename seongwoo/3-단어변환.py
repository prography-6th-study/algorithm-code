"""
dfs로 구현. 
begin부터 시작해서 words의 각 단어들을 비교해가며, 
단어가 하나만 다른 것 중 방문하지 않은 것을 다음 대상으로 두고, 단계값을 1씩 올려주는 식으로 구현.
방문 유무는 word가 dictionary에 있는지 유무로 판단.
"""

from collections import deque

def solution(begin, target, words):
    d = dict()
    d[begin] = 0
    q = deque([begin])
    
    while q:
        cur = q.popleft()
        for word in words:
            cnt = 0
            for i, j in zip(word, cur):
                if i != j:
                    cnt += 1
                if cnt == 2:
                    break
            if cnt == 1 and word not in d:
                q.append(word)
                d[word] = d[cur] + 1
    return d.get(target, 0)
    
b = "hit"
t = "cog"
w = ["hot", "dot", "dog", "lot", "log", "cog"]	

print(solution(b,t,w))
    