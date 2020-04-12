def solution(heights):
    answer = [0] * len(heights)
    while heights:
        right = heights.pop()
        for idx in range(len(heights)-1,-1,-1):
            if heights[idx] > right:
                answer[len(heights)] = idx+1
                break
    return answer