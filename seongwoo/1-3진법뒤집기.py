def convert(n, base):
    T = "012"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n):
    converted_n = (convert(n, 3))
    ret = 0
    for idx, ele in enumerate(converted_n):
        ret += 3 **(idx) * int(ele)
    return ret