"""
words 배열을 순회하면서 dictionary를 통해 
1. 중복인지
2. 단어의 길이가 1인지
3. 이전 단어의 끝 알파벳과 현재 단어의 시작 알파벳이 같은지 
를 확인하여 위 조건에 하나라도 해당되면 [번호, 차례]를 반환.
번호와 차례는 words 배열에서의 index를 사람수 n으로 나눈 나머지와 몫을 통해 도출하였음.
"""

def solution(n, words):
    d = dict()
    for idx, w in enumerate(words):
        if d.get(w, 0) or len(w) == 1:
            return [(idx % n) + 1, (idx // n) + 1]
        elif idx != 0:
            if w[0] != words[idx - 1][-1]:
                return [(idx % n) + 1, (idx // n) + 1]
            else:
                d[w] = 1
        else:
            d[w] = 1
    return [0, 0]