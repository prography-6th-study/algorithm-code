def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        # 비트 or 연산, 2진수 변환, 슬라이싱 -> zfill() 함수로 자리수 맞추기 -> #, " "로 대체
        result = bin(arr1[i] | arr2[i])[2:].zfill(n).replace("1", "#").replace("0", " ")
        answer.append(result)
    return answer


# test
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
print(solution(5, [0, 0, 0, 0, 0], [30, 1, 21, 17, 28]))