"""
풍선이 끝까지 남기 위해서는 이 풍선보다 작은 풍선이 없거나, 풍선의 왼쪽 오른쪽에 해당 풍선보다 큰 풍선이 존재해야함.
양쪽 끝값은 무조건 남길 수 있다.
left와 right는 자기보다 작은 숫자가 나타날 때 갱신됨
남는 풍선 = left에 갱신된 횟수 + right에 갱신된 횟수 + 양끝값 개수 - 1(중복)
"""

def solution(a):
    ret = 2
    if 0 <= len(a) <= 2:
        return len(a)
    left = a[0]
    right = a[-1]

    for i in range(1, len(a) - 1):
        if left > a[i]:
            left = a[i]
            ret += 1
        if right > a[-1 - i]:
            right = a[-1 - i]
            ret += 1
    if left == right:
        return ret - 1
    else:
        return ret
        
print(solution([9, -1, -5]))
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
