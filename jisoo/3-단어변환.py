import pytest
from collections import deque

def check_word(word1, word2):
    count = 0
    for w1, w2 in zip(word1, word2):
        if w1 != w2:
            count += 1
    if count == 1:
        return True
    return False

def solution(begin, target, words):
    if target not in words:
        return 0
    
    bfs = deque([begin])
    answer = 0

    while target not in bfs:
        temp = deque([])
        while bfs:
            now = bfs.popleft()
            for w in words:
                if check_word(now, w):
                    temp.append(w)
                    words.remove(w)
        bfs = temp   
        answer += 1

    return answer


@pytest.mark.parametrize("begin, target, words, expected", [
    ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 4),
    ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0)
])
def test_simple(begin, target, words, expected):
    assert solution(begin, target, words) == expected

"""
[ 풀이 방법 ]
- 가장 짧은 경로를 찾는거니까 bfs를 활용해서 풀어야 한다고 생각함
"""