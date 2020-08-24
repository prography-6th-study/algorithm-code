def solution(s):
    stack = [s[0]]  # 짝지어 제거하기 위한 스택 초기화
    # 문자열을 인덱스 1번째부터 끝까지 돌면서
    for i in s[1:]:
        stack.append(i)  # 스택에 추가
        # 스택의 원소가 2개 이상이고, 끝의 두 값이 같으면 제거
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    # 반복문을 돌고 나서 스택의 길이가 0이면 모두 제거된 경우
    if len(stack) == 0:
        return 1
    else:
        return 0

# test
print(solution("baabaa"))
print(solution("cdcd"))