from math import gcd

def solution(w,h):
    my_gcd = gcd(w, h)  # 가로, 세로의 최대공약수
    small_w, small_h = w // my_gcd, h // my_gcd   # 대각선 꼭지점을 지나는 작은 사각형의 가로, 세로
    x = small_w + small_h - 1  # 작은 사각형에서 못 쓰는 사각형의 개수
    return w * h - my_gcd * x  # 전체 사각형의 개수 - x * 최대공약수 (작은 사각형이 최대공약수 만큼 반복됨)

# test
print(solution(8, 12))
print(solution(3, 3))