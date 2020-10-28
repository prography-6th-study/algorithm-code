# 진법 변환해주는 함수
def conv(number, base):
    arr = "0123456789ABCDEF"
    q, r = divmod(number, base)
    if q == 0:
        return arr[r]
    else:
        return conv(q, base) + arr[r]

def solution(n, t, m, p):  # 진법, 구하는 수의 개수, 참가 인원, 튜브의 순서
    digits = ""
    number = 0
    # digits의 길이가 구하는 수의 개수 * 참가 인원 (t*m) 보다 커질 때까지 반복
    while len(digits) < t * m:
        digits += conv(number, n)  # 진법변환 후 digits에 추가
        number += 1
    answer = ""
    # 구하는 수의 개수 (t) 만큼 반복
    for i in range(t):
        answer += digits[(p - 1) + i * m]
    return answer


# test
print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))