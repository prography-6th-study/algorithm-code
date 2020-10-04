def solution(msg):
    d = dict()
    ret = []
    for i in range(26):
        d[chr(i + 65)] = i + 1
    cnt = 27
    while msg:
        idx = 1
        while msg[:idx] in d and idx <= len(msg):
            idx += 1
        ret.append(d[msg[:idx - 1]])
        d[msg[:idx]] = cnt
        cnt += 1
        msg = msg[idx - 1:]
    return ret

m = "KAKAO"
print(solution(m))