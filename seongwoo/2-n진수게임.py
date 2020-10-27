"""
말할 숫자들을 하나의 string으로 쭉 늘어놓고,
자기 순서가 될 때, 즉, idx % m == p - 1 일 때만 결과 ret에 붙여주는 식으로 구현
여기서 말할 숫자의 개수를 설정할 때 조금 애를 먹었는데, 문제에서 제시되는 충분히 큰 값인 t^2 값을 설정함으로 해결.
"""

def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n, t, m, p):
    num_str = ""
    ret = ""
    for i in range(t**2):
        num_str += convert(i, n)

    for idx, j in enumerate(num_str):
        if t == len(ret):
            return ret
        if idx % m == p - 1:
            ret += j
    return ret