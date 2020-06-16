from collections import deque

def check(word1, word2):
    count = 0
    for w1, w2 in zip(word1, word2):
        if w1 != w2:
            count += 1
    if count == 1:
        return True
    return False

def solution(begin, target, words):
    bfs = deque([begin])
    answer = 0
    
    if target not in words:
        return 0

    while target not in bfs:
        temp = deque([])
        while bfs:
            now = bfs.popleft()
            for w in words:
                if check(now, w):
                    temp.append(w)
                    words.remove(w)
        bfs = temp   
        answer += 1

    return answer

"""풀이방법
두 단어 비교해서 철자 하나 차이면 이어져있고 아니면 안 이어진 그래프에서 최단거리를 찾는다는 생각을 함
그래프 최단거리는 bfs
"""