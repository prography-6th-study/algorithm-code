def solution(N, number):
    # n개의 N으로 표현할 수 있는 수들의 집합을 담을 리스트 생성
    # 1~8 까지만 확인하면 된다
    arr = [set() for i in range(8)]

    for i, s in enumerate(arr, start=1):
        s.add(int(str(N) * i))   # 5, 55 ... N을 이어붙인 경우를 각 set에 저장

    # n번 set :
    # 1번 set (연산) n-1번 set U 2번 set (연산) n-2 set U ... U n-1번 set (연산) 1번 set
    # 이 부분을 이해하는 것이 아직 어렵다....
    for i in range(1, len(arr)):
        for j in range(i):
            for op1 in arr[j]:
                for op2 in arr[i - j - 1]:
                    arr[i].add(op1 + op2)
                    arr[i].add(op1 - op2)
                    arr[i].add(op1 * op2)
                    if op2 != 0:
                        arr[i].add(op1 // op2)

        if number in arr[i]:
            answer = i + 1
            break
        else:
            answer = -1
    print(arr)

    return answer


# test
print(solution(5, 12))
print(solution(2, 11))

# 너무 어려워서 다른 사람의 풀이를 참고했다.
# n번 set을 일반화하여 만드는 부분이 아직 이해가 되지 않는다..