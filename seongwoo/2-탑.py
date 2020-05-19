"""
배열의 각 element의 index를 기준으로 index를 -1 해가면서
자신의 높이보다 높은 탑이 있는지 확인한다.
"""

def solution(heights):
    answer = []
    for idx, ele in enumerate(heights):
        if idx == 0:
            answer.append(0)
            continue
        flag = False
        for i in range(idx,-1,-1):
            if heights[i] > ele:
                answer.append(i+1)
                flag = True
                break
        if flag == False:
            answer.append(0)
    return answer