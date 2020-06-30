def solution(arrangement):
    bars = 0  # 막대기 개수
    answer = 0  # 잘려나간 막대기 개수
    arrangement = list(arrangement)

    while arrangement:
        # ( : 막대기 추가
        if arrangement[0] == "(":
            arrangement.pop(0)
            bars += 1
            # () : 막대기 추가가 아닌 레이저 쏨
            if arrangement[0] == ")":
                arrangement.pop(0)
                bars -= 1  # 위에서 막대기 추가했기 때문에 다시 제거
                answer += bars  # 레이져를 쏘면 막대기 개수만큼 잘린 막대기 개수가 증가
        # ) : 막대기 삭제, 막대기 개수 +1
        else:
            arrangement.pop(0)
            bars -= 1
            answer += 1  # 제거한 막대기 1개 추가

    return answer

# test
print(solution("()(((()())(())()))(())"))


