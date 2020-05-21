def solution(n, times):
    left = 1
    right = max(times)*n # 최악의 경우
    
    while(left <= right):
        average = (left+right)//2
        total = sum([ average//time for time in times ])
        if total < n: # 모든 사람을 심사할 수 없는 경우
            left = average + 1
        else: #모든 사람을 심사할 수 있는 경우
            right = average - 1
    return left

"""풀이방법
어떤 값을 이분탐색할 것인지 + 기준은 뭘로 잡을지에 대한 감이 안 잡혔다.
한명의 심사관에게 얼만큼의 시간을 줄지로 잡았다
"""