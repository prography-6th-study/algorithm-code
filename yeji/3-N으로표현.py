def solution(N, number):
    S = [0, {N}]
    for i in range(2, 9):
        case_set = {int(str(N)*i)}
        for i_half in range(1, i//2+1):  # S[i_half] S[1]
            for x in S[i_half]:
                for y in S[i-i_half]:
                    case_set.add(x+y)
                    case_set.add(x-y)
                    case_set.add(y-x) # y-x 케이스 추가
                    case_set.add(x*y)
                    if x != 0:
                        case_set.add(y//x)
                    if y != 0:
                        case_set.add(x//y)
        if number in case_set:
            return i
        S.append(case_set)
        print(S)
    return -1

"""
풀이방법
- 다른 사람 풀이 참고
- 규칙 찾는데도 오래걸리고 풀이보고 이해하는것도 오래걸렸다ㅠ
N을 n번 사용해서 만들 수 있는 수 :
N을 n번 연달아서 사용할 수 있는 수 U
N을 1번 사용했을 때 SET 과 n-1번 사용했을 때 SET을 사칙연산한 수들의 집합 U
N을 2번 사용했을 때 SET 과 n-2번 사용했을 때 SET을 사칙연산한 수들의 집합 U
... U
N을 n-1번 사용했을 때 SET 과 1번 사용했을 때 SET을 사칙연산한 수들의 집합
"""
