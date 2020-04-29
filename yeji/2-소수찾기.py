from itertools import permutations

def solution(numbers):
    answer = set()
    maximum = 10000000
    #0,1은 소수가 아니고 2는 소수
    prime = [False, False] + [True] * maximum
    #에라토스의 체
    for idx, num in enumerate(prime):
        if num: #num이 true면
            k = idx*2
            while k <= maximum:
                prime[k] = False
                k += idx
    
    for i in range(1, len(numbers)+1):
        case = permutations(list(numbers), i)
        for j in list(case):
            num = int("".join(list(j)))
            #prime 배열에서 해당 수가 소수인지 아닌지 판별
            if prime[num]:
                answer.add(num)
    return len(answer)

"""풀이방법
통과는 했는데 좋은 방법이라곤 생각 안 한당
"""