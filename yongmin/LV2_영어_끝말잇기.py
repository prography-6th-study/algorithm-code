def solution(n, words):
    result = [0, 0]
    used = [words[0]]  # 사용한 단어 리스트 초기화

    # words의 인덱스 1부터 끝까지
    for i in range(1, len(words)):
        # 이전 단어의 끝글자와 현재 단어의 첫글자 같고 현재 단어가 사용한 적 없으면 used에 추가
        if words[i-1][-1] == words[i][0] and words[i] not in used:
            used.append(words[i])
        # 탈락한 경우
        else:
            result[0] = i % n + 1  # 탈락한 사람의 번호
            result[1] = i // n + 1  # 탈락한 회차
            break

    return result


# test
print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"] ))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage",
                  "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))