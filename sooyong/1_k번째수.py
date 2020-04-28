def solution(array, commands):
    ans = []
    for item in commands:
        ans.append(sorted(array[item[0]-1:item[1]])[item[2]-1])
    return ans
