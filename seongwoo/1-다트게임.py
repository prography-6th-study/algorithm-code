"""
처음에 접근은 while문을 돌면서 idx, idx + 1, idx + 2 의 문자를 비교하는 것으로 했는데, 
아무래도 10 같은 경우에 처리가 불편했고, 그 다음에는 스택을 사용해서 풀이했다.

테스트케이스 18번 22번이 통과가 안되었는데, 이것은 이전에 *가 두번 연속으로 나오는 경우에 대한 처리를 
안해주었기 때문에 발생했다. 
s.append(num * 2 + s.pop() * 2) 이 코드를 지우고
s.append(s.pop() * 2)
s.append(num * 2)
로 따로 스택에 넣음으로 해결하였다. 
"""


def solution(dartResult):
    s = []
    flag = False
    for idx, i in enumerate(dartResult):
        if flag == True:
            flag = False
            continue
        if i == '1' and dartResult[idx + 1] == '0':
            tmp = 10
            flag = True
        elif i in [str(n) for n in range(0, 10)]:
            tmp = int(i)
        elif i == 'S':
            s.append(tmp)
        elif i == 'D':
            s.append(tmp ** 2)
        elif i == 'T':
            s.append(tmp ** 3)
        elif i == '*':
            num = s.pop()
            if s == []:
                s.append(num * 2)
            else:
                s.append(s.pop() * 2)
                s.append(num * 2)
        elif i == '#':
            tmp = s.pop() * (-1)
            s.append(tmp)
    return sum(s)


print(solution('1D2S0T'))
