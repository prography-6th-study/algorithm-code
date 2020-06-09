"""
스택을 사용하는 것이 직관적으로 떠오르지 않았음.
다른 사람의 코드를 참고해서 풀었다. 
"""

def solution(number, k):
    s = []
    for i in number:
        while len(s) != 0 and s[-1] < i and k > 0: # 스택의 top 값이 비교하는 값보다 작을 때 pop
            k -= 1
            s.pop()
        s.append(i)
    if k != 0: # for testcase 12
        s = s[:-k]
    return "".join(s)
    

print(solution("4177252841", 4))
print(solution("1000", 2)) # 12번 테스트케이스