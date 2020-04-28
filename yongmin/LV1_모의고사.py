# 모의고사
def solution(answers):
    # 수포자들의 찍기 패턴
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0, 0, 0] # 수포자들이 맞춘 갯수
    index = 0
    for answer in answers:
        if answer == first[index % len(first)]:
            scores[0] += 1
        if answer == second[index % len(second)]:
            scores[1] += 1
        if answer == third[index % len(third)]:
            scores[2] += 1
        index += 1

    result = []
    for i in range(len(scores)):
        if scores[i] == max(scores):
            result.append(i+1)

    return result


# test
print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))