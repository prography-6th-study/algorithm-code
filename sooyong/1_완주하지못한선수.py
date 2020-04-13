def solution(participant, completion):
    answer = ''
    d= dict()
    # register participant
    for item in participant:
        if item in d:
            d[item] +=1
        else:
            d[item] = 1

    # remove completion
    for item in completion:
        if d[item] == 1:
            del d[item]
        else:
            d[item] -= 1
    for item in d.keys():
        answer = item
    return answer
