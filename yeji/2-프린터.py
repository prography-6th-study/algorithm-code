def solution(priorities, location):
    answer = 0
    m = max(priorities)
    while True:
        top = priorities.pop(0)
        if top is m:
            answer += 1
            if location is 0:
                break
            else:
                location -= 1
            m = max(priorities)
        else:
            priorities.append(top)
            if location is 0:
                location = len(priorities)-1
            else:
                location -= 1
    return answer