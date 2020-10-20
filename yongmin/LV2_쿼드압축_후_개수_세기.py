result = []

def check(n, x, y, arr):
    num = arr[x][y]  # 기준값
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 하나라도 다른 원소가 있으면 다시 4개로 나누어 실행
            if num != arr[i][j]:
                check(n//2, x, y, arr)
                check(n//2, x, y + n//2, arr)
                check(n//2, x + n//2, y, arr)
                check(n//2, x + n//2, y + n//2, arr)
                return
    result.append(num)

def solution(arr):
    n = len(arr)  # 정사각형 한 변의 길이
    check(n, 0, 0, arr)
    answer = [0, 0]
    for v in result:
        if v == 0:
            answer[0] += 1
        else:
            answer[1] += 1
    return answer


# test
print(solution([[1, 1, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 1],
                [1, 1, 1, 1]]))
print(solution([[1, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 1, 1, 1, 1],
                [0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 1, 1]]))
