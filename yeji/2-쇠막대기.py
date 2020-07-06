def solution(arrangement) :
    arrangement = list(arrangement)
    temp = list()
    x = 0 
    cnt = 0
    for i in range(len(arrangement)) :
        a = arrangement.pop(0)
        if a == "(" :
            x+=1 
            cnt+=1
        else :
            if temp[-1] == "(" :
                x-=1 
                cnt-=1 
                cnt+=x
            else :
                x-=1
        temp.append(a)
    return cnt

"""풀이방법
x가 안잘려진 막대기의 수, cnt가 잘려진 막대기의 수

"("이면 일단 막대기가 하나 더 놓아졌다고 생각해 x와 cnt에 각각 +1

이후 들어오는 문자가 ")"이면 이것이 레이저를 뜻하는지, 막대의 끝점인지 확인
-> temp[-1]가 "(" 라면 레이저, ")"라면 막대

레이저를 뜻한다면 막대가 하나 더 놓아진 것이 아니기 때문에 +1 해준것을 그대로 다시 빼주고, 잘린 막대의 수를 cnt에 더하기
"""