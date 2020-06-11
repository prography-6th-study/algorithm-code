from itertools import permutations

def check_num(check, num):
    strike, ball = 0, 0
    for i in range(len(num)):
        # 자리수와 숫자가 같으면 스트라이크
        if check[i] == num[i]:
            strike += 1
        # 자리는 다르지만 숫자가 포함되면 볼
        elif check[i] in num:
            ball += 1
    return strike, ball

def solution(baseball):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    all = list(map(''.join, permutations(numbers, 3)))  # 가능한 모든 순열 구하기
    # baseball을 돌면서
    for num, strike, ball in baseball:
        # 조건에 맞는 값들만 남긴다
        all = [ check for check in all if check_num(check, str(num)) == (strike, ball) ]
    return len(all)




# test
print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))