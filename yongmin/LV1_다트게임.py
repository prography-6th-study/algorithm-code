def solution(dartResult):
    result = []
    num = ""
    for s in dartResult:
        if s.isnumeric():  # 숫자값이면 num에 추가
            num += s
        elif s == "S":  # result에 추가하고 num 초기화
            result.append(int(num))
            num = ""
        elif s == "D":  # result에 제곱하여 추가하고 num 초기화
            result.append(int(num) ** 2)
            num = ""
        elif s == "T":  # result에 3제곱하여 추가하고 num 초기화
            result.append(int(num) ** 3)
            num = ""
        elif s == "*":  # 스타상
            if len(result) == 1:  # 1회차인 경우
                result[0] = result[0] * 2
            else:
                result[-1] = result[-1] * 2
                result[-2] = result[-2] * 2
        elif s == "#":  # 아차상
            result[-1] = -result[-1]

    return sum(result)


# test
print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))
