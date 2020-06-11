def solution(people, limit):
    count = 0 # 배 하나에 둘이 타는 경우
    people.sort()
    light = 0 # 가장 가벼운 사람 위치
    heavy = len(people)-1 # 가장 무거운 사람 위치

    while( light < heavy ):
        if people[light] + people[heavy] <= limit :
            count += 1
            light += 1
            heavy -= 1
        else:
            heavy -= 1

    boat = len(people) - count
    
    return boat