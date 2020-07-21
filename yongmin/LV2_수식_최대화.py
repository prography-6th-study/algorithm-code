import itertools


def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))


def calculate(expression, op):
    cal_tmp = []
    print(op)
    for i in expression:
        if not i in op:
            if len(cal_tmp) != 0 and not cal_tmp[-1] in op:
                cal_tmp[-1] = cal_tmp[-1] + i
            else:
                cal_tmp.append(i)
        else:
            cal_tmp.append(i)

    result = []
    stack = []
    for o in op:
        while True:
            if len(cal_tmp) == 0:
                break
            tmp = cal_tmp.pop(0)
            if tmp == o:
                stack.append(operation(stack.pop(-1), cal_tmp.pop(0), o))
            else:
                stack.append(tmp)
        result.append(stack)
        cal_tmp = stack
        stack = []

    return result[-1]


def solution(expression):
    op = ['+', '-', '*']
    op = list(itertools.permutations(op, 3))
    answer = 0
    for i in op:
        answer = max(answer, abs(int(calculate(expression, i)[0])))
    return answer


# test
print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))