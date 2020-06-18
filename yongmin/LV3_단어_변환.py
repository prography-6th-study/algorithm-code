def solution(begin, target, words):
    # words 안에 target이 없으면 0 리턴
    if target not in words:
        return 0

    total = 0  # 변환 횟수
    queue = [begin]
    # words 안에 요소가 있을 동안 반복
    while words:
        # queue 요소들을 순회
        for value in queue:
            temp = []  # 바꾸게 될 단어를 저장하는 리스트
            for word in words:
                count = 0
                for i in range(len(word)):
                    # 단어의 인덱스 값이 다르면 count 1 증가
                    if value[i] != word[i]:
                        count += 1
                    # 단어의 인덱스 값이 다른게 2개 이상이면 x
                    if count == 2:
                        break
                # 다른 값이 1개라면 변환이 가능하므로
                if count == 1:
                    temp.append(word)
                    words.remove(word)
        #print(temp, total)
        total += 1  # 변환횟수 +1
        # target값과 같아면 변환이 끝났으므로 total 리턴
        if target == "".join(temp):
            return total
        # temp 값을 큐에 넣고 다시 반복
        else:
            queue = temp


# test
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
print(solution("hit", "hhh", ["hhh", "hht"]))