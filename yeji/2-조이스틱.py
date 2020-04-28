import string

def solution(name):
    carser = [ min( ord(n)-ord("A") , ord("Z")-ord(n)+1 ) for n in name ]
    answer = 0
    position = 0

    while True:
        answer += carser[position]
        carser[position] = 0

        if sum(carser) == 0:
            break

        left, right = (1, 1)

        while carser[position - left] <= 0:
            left += 1
            print(left)

        while carser[position + right] <= 0:
            right += 1
            print(right)

        answer += left if left < right else right
        position += -left if left < right else right

        print(position)

    return answer

solution("JAZ")