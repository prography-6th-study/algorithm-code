"""
가장 어려웠던 문제였고 다른 사람 풀이 참조해서 풀었음.
operand로 쓰이는 N의 개수를 1개부터 8개까지 test 해가면서 사칙연산한 값 중에서 target 값이 있다면, 
해당 N의 개수를 반환
"""

def solution(N, number):
    arr = [set() for _ in range(8)]
    for idx, i in enumerate(arr):
        i.add(int(str(N) * (idx+1)))
    print(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            for x in arr[j]:
                for y in arr[i-j-1]:
                    if y == 0:
                        arr[i].update([x + y, x - y, x * y])
                    else:
                        arr[i].update([x + y, x - y, x * y, x // y])
        if number in arr[i]:
            return i + 1
    return -1

print(solution(5,12))