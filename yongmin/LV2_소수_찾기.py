from itertools import permutations  # 순열

def solution(numbers):
    answers = set()
    max_num = 10000000

    # 소수찾기 : 에라토스테네스의 체
    primes = [False, False] + [True] * max_num
    for num, is_prime in enumerate(primes):
        # 처음 나타나는 수의 배수를 모두 지움
        if is_prime:
            k = num * 2
            while k <= max_num:
                primes[k] = False
                k += num

    for i in range(1, len(numbers) + 1):
        P = permutations(list(numbers), i) # 순열 구하기
        for value in list(P):
            n = int("".join(list(value)))
            if primes[n]:  # 소수 판별
                answers.add(n)

    return len(answers)




# test
print(solution("17"))
print(solution("011"))


