"""
짝수일 때는 순간이동이 가능하므로 나누기 2를 해주었고
홀수일 때는 움직이는 비용이 소모되기 때문에 cnt를 늘리고 -1 해주었다.
"""

def solution(n):
    cnt = 0
    while n != 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n -= 1
            cnt += 1
    return cnt