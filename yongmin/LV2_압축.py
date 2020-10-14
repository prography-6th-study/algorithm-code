def solution(msg):
    # 사전 초기화
    d = dict()
    for i in range(1, 27):
        d[chr(i+64)] = i

    num = 27  # 색인 번호
    answer = []
    while msg:
        idx = 0
        # 사전에서 msg 처음부터 일치하는 가장 긴 문자열의 끝 찾기
        for i in range(1, len(msg) + 1):
            if msg[:i] in d:
                idx = i
        answer.append(d[msg[:idx]])  # w에 해당하는 사전의 색인 번호 출력
        d[msg[:idx + 1]] = num  # w + c 에 해당하는 단어를 사전에 등록
        num += 1  # 색인번호 +1
        msg = msg[idx:]  # 입력에서 w를 제거

    return answer


#print(ord("A"))  # 65
#print(chr(65))  # A

# test
print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))