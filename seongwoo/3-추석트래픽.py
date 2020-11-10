# activity selection problem -> greedy
# 요청 개수가 바뀔 때 - 새 요청이 들어오거나 요청이 끝날 때

import datetime

def solution_mine(lines):
    new_li = []
    cnt = 0
    for line in lines:
        day, time, process = map(str, line.split())
        new_time = str(datetime.datetime.strptime(time, '%H:%M:%S.%f') + datetime.timedelta(seconds=float(process[:-1])))
        new_time = new_time.split()[1]
        new_li.append((time, new_time))
    print(new_li)
    if len(new_li) == 1:
        return 1
    s, e = new_li[0][0], new_li[-1][1]
    while s <= e:
        s = str(datetime.datetime.strptime(time, '%H:%M:%S.%f') + datetime.timedelta(seconds=1))
        cnt += 1
    return cnt
                
def solution(lines):
    starts, ends = [], []
    for line in lines:
        day, time, process = map(str, line.split())
        end = day + "T" + time
        end = datetime.datetime.fromisoformat(end)
        process = datetime.timedelta(seconds=float(process[:-1]))
        start = end - process + datetime.timedelta(seconds=0.001)
        starts.append(start)
        ends.append(end)

    new_li = starts + ends # 요청 개수가 바뀔 때 : 새 요청이 들어오거나 요청이 끝날 때  <- 이 때만 1초 동안 개수 늘어나는지 확인
    ret = 0
    second = datetime.timedelta(seconds = 1)
    for start in new_li:
        cnt = 0
        for i in range(len(ends)):
            if start <= ends[i] < start + second or start <= starts[i] < start + second: # 1초사이에 다른 작업이 끝나거나, 시작한다면 cnt++
                cnt += 1
            elif ends[i] <= start and starts[i] >= start + second: # 새로운 작업 전체가 1초 안에 포함되는 경우 cnt++
                cnt += 1
        ret = max(ret, cnt)
    return ret
        
        
