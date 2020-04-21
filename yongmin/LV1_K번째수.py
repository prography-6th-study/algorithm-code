def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        temp = sorted(array[i-1:j]) # i-1부터 j-1까지 슬라이싱하여 정렬한 리스트 반환
        answer.append(temp[k-1]) # answers에 k-1번째 원소 추가
    return answer


#test
print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))