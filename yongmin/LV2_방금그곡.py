import datetime

def change(m):
    m = m.replace("C#", "c")
    m = m.replace("D#", "d")
    m = m.replace("F#", "f")
    m = m.replace("G#", "g")
    m = m.replace("A#", "a")
    return m

def solution(m, musicinfos):
    answer = "(None)"
    length = 0  # 정답 후보의 재생 시간
    for info in musicinfos:
        # 시작시간, 종료시간, 곡 제목, 악보
        start, end, title, melody = info.split(',')
        s = datetime.datetime.strptime(start, '%H:%M')
        e = datetime.datetime.strptime(end, '%H:%M')
        minutes = (e - s).seconds // 60  # 재생시간 (분)

        # 악보와 기억한 멜로디에 대해서 # 처리
        melody = change(melody)
        m = change(m)

        # 라디오에서 재생된 멜로디
        play = ""
        for i in range(minutes):
            play += melody[i % len(melody)]

        # 기억한 멜로디가 라디오에서 재생된 멜로디에 포함 and 현재 곡의 재생시간이 더 길면
        if m in play and minutes > length:
            length = minutes
            answer = title

    return answer


# test
print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
