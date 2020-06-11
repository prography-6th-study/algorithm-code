"""
yellow는 i * j, brown는 2i + 2j + 4 (변 2개 + 가장자리) 를 만족하는 i, j 값을 찾았다.
"""

def solution(brown, yellow):
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            j = yellow // i
            if 2*(i + j) + 4 == brown:
                return [j + 2, i + 2]

print(solution(10,2))