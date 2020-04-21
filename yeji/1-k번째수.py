def solution(array, commands):
    answer = []
    for x in commands:
        temp = array[x[0]-1:x[1]]
        k = x[2]-1
        temp.sort()
        answer.append(temp[k])
    return answer