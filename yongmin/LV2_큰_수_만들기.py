# 나의 풀이.. 시간초과로 실패
#def solution(number, k):
#    phase = 0
#    while phase != k:  # k번 반복
#        lst = []  # 후보들을 담을 리스트
#        phase += 1
#        for j in range(len(number)):
#            temp = list(number)  # number을 리스트로 변환한 후
#            temp.pop(j)  # j번 요소의 값을 삭제하고
#            lst.append(''.join(temp))  # 남은 요소들을 join한 값을 리스트에 담는다
#        number = str(max(lst))  # 리스트에서 가장 큰 값을 number로 재설정
#    return number

def solution(number, k):
    stack = []  # 자릿수를 담을 스택 생성

    # number의 각 자릿수를 순회
    for num in number:
        # number로 부터 자릿수를 하나씩 꺼내서 스택에 넣어준다
        # 다만 스택에 쌓인 것들이 지금 넣어줄 자릿수보다 작은 것들은 빼준다
        while stack and stack[-1] < num and k > 0:
            stack.pop()  # pop을 해주고
            k -= 1  # k를 1 줄인다
        stack.append(num)

    # k > 0 이라면 아직 제거 횟수를 다 사용하지 않은 경우
    # k만큼 뒷 부분을 잘라준다
    if k != 0:
        stack = stack[:-k]

    return ''.join(stack)

# test
print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))