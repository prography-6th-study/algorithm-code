"""
순열을 돌면서, 각 자리의 수가 일치할 때는 c_s (strike count)를 +1, 이후 element[1] 값과 다르다면 조건을 만족하지 않으므로 pass.
똑같은 형식으로 숫자가 자리만 다를 경우에 c_b (ball count)를 +1, element[2] 값과 다르다면 제외.
모든 질문을 확인했을 때 조건을 다 만족했다면 카운트 값을 +1 해주었다.
"""

from itertools import permutations

def solution(baseball):
    ret = 0
    li = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
    for ele in li:
        x, y, z = map(str, ele)
        for idx, (num, s, b) in enumerate(baseball):
            c_s, c_b = 0 , 0
            cx, cy, cz = map(str, str(num))

            if cx == x: c_s += 1
            if cy == y: c_s += 1
            if cz == z: c_s += 1
            if c_s != s: break

            if cy == x or cz == x: c_b += 1
            if cx == y or cz == y: c_b += 1
            if cx == z or cy == z: c_b += 1
            if c_b != b: break

            if idx + 1  == len(baseball):
                ret += 1
    return ret

print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))
