def solution(numbers):
    s = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            s.append(numbers[i] + numbers[j])
    return sorted(list(set(s)))