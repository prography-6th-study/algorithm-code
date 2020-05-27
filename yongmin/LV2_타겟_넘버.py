def solution(numbers, target):
    p_list = [0]  # 부모 노드 리스트

    for num in numbers:
        c_list = []   # 자식 노드 리스트
        # 부모 노드에 num을 더하고 빼준 것을 자식 노드에 추가
        for v in p_list:
            c_list.append(v + num)
            c_list.append(v - num)
        p_list = c_list   # 자식노드 -> 부모노드

    return p_list.count(target)  # 모든 연산이 끝난 리스트에서 target 값을 count


# test
print(solution([1, 1, 1, 1, 1], 3))