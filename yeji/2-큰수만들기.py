def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1 # 숫자 제거 남은 횟수
            stack.pop() # 작은 수 빼버림
        stack.append(num) # 큰 수 다시 집어 넣음
    if k != 0: #제거 횟수를 다 사용하지 않았을때 남은 횟수만큼 리스트 뒷부분을 잘라줌
        stack = stack[:-k] 
    return ''.join(stack)


solution("1924", 2)