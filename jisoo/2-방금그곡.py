from datetime import datetime

import pytest


def change_code(info):
    info = info.replace('C#', 'c')
    info = info.replace('D#', 'd')
    info = info.replace('F#', 'f')
    info = info.replace('G#', 'g')
    info = info.replace('A#', 'a')
    return info


def calculate_time(start, end):
    hour, minute, _ = str(datetime.strptime(end, '%H:%M') - datetime.strptime(start, '%H:%M')).split(':')
    time = int(hour) * 60 + int(minute)
    return time


def create_full_infos(infos, time):
    if time < len(infos):
        full_infos = infos[:time]
    else:
        q = time // len(infos)
        r = time % len(infos)
        full_infos = infos*q + infos[:r]
    return ''.join(full_infos)


def solution(m, musicinfos):
    m = change_code(m)
    answer = dict()
    for music_info in musicinfos:
        start, end, title, info = music_info.split(',')

        infos = change_code(info)
        time = calculate_time(start, end)

        full_infos = create_full_infos(infos, time)
        if m in full_infos:
            if time not in answer:
                answer[time] = title

    if len(answer) == 0:
        return '(None)'

    answer = sorted(answer.items(), reverse=True)
    return answer[0][1]



@pytest.mark.parametrize("m, musicinfos, expected", [
    ("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"], "HELLO"),
    ("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"], 'FOO'),
    ("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"], "WORLD")
])
def test_simple(m, musicinfos, expected):
    assert solution(m, musicinfos) == expected

"""
[ 풀이 방법 ]
- 문자열을 재생시간만큼 반복시켜서 m이 그 문자열에 포함되어있는지 구함
"""