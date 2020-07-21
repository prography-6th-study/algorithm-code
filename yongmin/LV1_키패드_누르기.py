key_pad = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           ["*", 0, "#"]]

# 왼손에서의 거리와 오른손에서의 거리 구하기
def calculate_distance(left, right, number):
    left_idx, right_idx, center_idx = [0, 0], [0, 0], [0, 0]
    for i in range(4):
        for j in range(3):
            if key_pad[i][j] == number:
                center_idx = [i, j]
            if key_pad[i][j] == left:
                left_idx = [i, j]
            if key_pad[i][j] == right:
                right_idx = [i, j]
    left_dist = abs(center_idx[0] - left_idx[0]) + abs(center_idx[1] - left_idx[1])
    right_dist = abs(center_idx[0] - right_idx[0]) + abs(center_idx[1] - right_idx[1])
    return left_dist, right_dist


def solution(numbers, hand):
    left, right = "*", "#"  # 왼손과 오른손의 위치
    left_side, right_side = [1, 4, 7], [3, 6, 9]  # 왼쪽과 오른쪽에 있는 숫자들

    answer = ""
    for number in numbers:
        # 왼쪽에 있는 숫자들이면 +L
        if number in left_side:
            answer += "L"
        # 오른쪽에 있는 숫자들이면 +R
        elif number in right_side:
            answer += "R"
        # 왼쪽에서의 거리와 오른쪽에서의 거리 구한 후 비교
        else:
            left_dist, right_dist = calculate_distance(left, right, number)
            if left_dist > right_dist:
                answer += "R"
            elif left_dist < right_dist:
                answer += "L"
            # 왼쪽과 오른쪽 거리가 같은 경우
            else:
                if hand == "left":
                    answer += "L"
                else:
                    answer += "R"

        # 이동한 손의 위치 지정
        if answer[-1] == "L":
            left = number
        else:
            right = number

    return answer



# test
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))