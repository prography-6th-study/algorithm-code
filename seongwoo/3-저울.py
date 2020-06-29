"""
weight 배열을 오름차순으로 정렬하고,
해당 배열을 순회하면서, 각 element가 (누적합+1) 보다 큰 경우 (누적합+1) 인 값을 만들 수 없기 때문에
해당 값을 return 해준다. 아닌 경우에는 element를 누적합에 더해준다.
"""


def solution(weight):
    weight.sort()
    s = 0
    for i in weight:
        if i > s + 1:
            return s + 1
        else:
            s += i
    return s + 1


w = [3, 1, 6, 2, 7, 30, 1]
print(solution(w))
