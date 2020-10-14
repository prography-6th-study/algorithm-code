```python
# 음악을 꾸며보자.
def makeMusic(musicinfos):
    table = [[block for block in row.split(",")] for row in musicinfos]
    return table

# 얼만큼 노래했는지 알아보자
def songTime(start_time, end_time):
    hour1, min1 = start_time.split(":")
    hour2, min2 = end_time.split(":")
    return abs(int(hour1)-int(hour2))*60 + abs(int(min2)-int(min1))

def solution(m, musicinfos):
    answer = ''
    table = makeMusic(musicinfos)   # 음악 구분하기
    # 시작시간, 끝나는 시간차이 구하기.
    for info in table:
        start_time = info[0]
        end_time = info[1]
        title = info[2]
        song = info[3]
        song_time = songTime(start_time,end_time)
        tmp = song * (song_time//len(song)) + song[:(song_time%len(song))]
        for idx in range(len(tmp)-len(m)+1):
            answ = tmp[idx:idx+len(m)]
            if m == answ:
                if tmp[idx+1]!="#":
                    answer = title
    return answer
```

