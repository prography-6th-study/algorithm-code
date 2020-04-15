def solution(heights):
    answer = []
    truck_num = len(heights)

    while len(heights) > 0:
        temp = heights.pop()

        for i in range(len(heights), 0, -1):
            if temp < heights[i-1]:
                answer.insert(0, i)
                break

        if len(heights) + len(answer) != truck_num:
            answer.insert(0, 0)

    return answer


#test
h1 = [6, 9, 5, 7, 4]
h2 = [3, 9, 9, 3, 5, 7, 2]
h3 = [1, 5, 3, 6, 7, 6, 5]

print(solution(h1))
print(solution(h2))
print(solution(h3))