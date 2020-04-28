def solution(n, lost, reserve):
    # 학생들의 체육복 현황
    students = [1] * n
    for n in lost:
        students[n-1] -= 1
    for n in reserve:
        students[n-1] += 1

    for i, n in enumerate(students):
        if n != 0:
            continue
        # 기준에서 왼쪽부터 탐색해야 최적해가 나온다
        if i > 0 and students[i-1] == 2:
            students[i-1] -= 1
            students[i] += 1
        elif i < len(students)-1 and students[i+1] == 2:
            students[i+1] -= 1
            students[i] += 1

    return len(students) - students.count(0)



# test
print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))