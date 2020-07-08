def solution(s):
    answer = ""

    # 한 글자 예외처리
    if len(s) == 1:
        return 1

    # 1부터 문자열길이//2+1 까지만 반복
    for n in range(1, (len(s)//2)+1):
        # 문자열 s를 n개씩 잘라 splited에 담는다
        splited = []
        for i in range(0, len(s), n):
            temp = s[i:n+i]  # n개씩 자른 문자열
            # 첫 번째 자른 값을 넣어줌
            if len(splited) == 0:
                splited.append(temp)
                splited.append(1)
                continue
            # -2에는 자른 값, -1에는 값의 개수
            if splited[-2] == temp:
                splited[-1] += 1
            else:
                splited.append(temp)
                splited.append(1)

        compact = ""  # 압축한 문자열
        for v in splited:
            # 개수가 1이면 압축 문자열에 개수를 넣지 않음
            if v == 1:
                continue
            compact += str(v)

        # 첫번째 값 answer로 설정
        if answer == "":
            answer = compact
            continue
        # 압축한 문자열의 길이가 더 작으면 answer를 바꿔준다
        if len(compact) < len(answer):
            answer = compact

    return len(answer)

# test
print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution(("a")))
