def solution(name):
    count = 0
    where = 0
    # 상하 조작의 최소 횟수 : char-'A'와 'Z'-char+1 중에서 작은 값을 고른다
    lst = [ min(ord(char) - ord('A'), ord('Z') - ord(char) + 1) for char in name ]

    while True:
        count += lst[where]
        lst[where] = 0

        if sum(lst) == 0: # 조작이 끝난 경우,
            # 반복 종료
            break

        # 좌우 조작의 최소횟수 구하기
        left, right = 1, 1
        while lst[where - left] <= 0:
            left += 1
        while lst[where + right] <= 0:
            right += 1

        if left < right:
            count += left
            where += -left
        else:
            count += right
            where += right

    return count




# test
print(solution('JEROEN'))
print(solution('JAN'))