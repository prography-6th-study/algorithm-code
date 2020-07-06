"""
카메라를 추가해야하는 시점은 카메라 위치가 이전 범위에 포함이 되지 않을 때.
시작지점이나 끝나는 지점을 순서대로 정렬하여 비교하면 범위를 쉽게 확인 가능.
아래 풀이는 시작지점을 정렬하여 이전 범위에 포함되는지를 확인하는 코드임
"""


def solution(routes):
    cnt, pre = 0, 30000
    return sorted(routes, reverse=True)
    for r in sorted(routes, reverse=True):
        if pre > r[1]:  # 이전 범위에 포함이 안 되면
            cnt += 1
            pre = r[0]
    return cnt


r = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
print(solution(r))
