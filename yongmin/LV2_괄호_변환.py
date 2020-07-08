# 주어진 문자열을 두 균형잡인 괄호 문자열로 나눠주는 함수
def split_str(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] == "(":
            cnt += 1
        elif s[i] == ")":
            cnt -= 1
        if cnt == 0:
            return s[:i+1], s[i+1:]


# 올바른 괄호 문자열인지 확인하는 함수
def is_correct(s):
    cnt = 0
    for v in s:
        if v == "(":
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    if cnt != 0:
        return False
    return True


def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열 반환
    if not p:
        return p

    # 2. 문자열을 두 균형잡인 괄호 문자열 u, v로 분리
    u, v = split_str(p)

    # 3. u가 올바른 괄호 문자열이라면 v에 대해 1단계부터 다시 수행
    if is_correct(u):
        # 3-1 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
        return u + solution(v)
    # 4. 그게 아니라면
    else:
        temp = "("  # 4.1 빈 문자열에 첫 번째 문자로 '('를 붙인다
        temp += solution(v)  # 4-2 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙인다
        temp += ")"  # 4-3 ')'를 다시 붙인다
        u = list(u[1:-1])  # 4-4 u의 첫 번째와 마지막 문자를 제거하고
        # 4-4 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙인다
        for v in u:
            if v == "(":
                temp += ")"
            elif v == ")":
                temp += "("
        # 4-5 생성된 문자열을 반환
        return temp


# test
print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))