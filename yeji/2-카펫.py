import math

def solution(brown, yellow):
    total = brown + yellow # 카펫 넓이
    carpet = [] # 카펫 가로, 세로 담을 배열

    sq = int(math.sqrt(total)) #제곱근

    for i in range(3,sq+1): #세로는 제곱근 보다 커질 수 없음
        height = i
        width = total//i

        if (height*width) == total:
            yellow_w = width-2 # 양 옆 브라운 두개 빼주기
            yellow_h = height-2 # 위 아래 브라운 두개 빼주기

            if (yellow_h*yellow_w) == yellow:
                carpet.append(width)
                carpet.append(height)
                break

    return carpet