"""
30번 테스트케이스만 찾지 못해서 참조했다.
30번 테스트케이스는 아래 입력 예시와 같이, 악보의 전체가 아니라 악보[:time] 만큼의 부분에서 m이 존재함을 체크해야 함.
"""

def solution(m, musicinfos):
    m = m.replace("C#", 'H').replace("D#", 'I').replace("F#", 'J').replace("G#", 'K').replace("A#", 'L')
    ret = []
    for info in musicinfos:
        s, e, name, sheet = info.split(',')
        sheet = sheet.replace("C#", 'H').replace("D#", 'I').replace("F#", 'J').replace("G#", 'K').replace("A#", 'L')
        sh, sm = map(int, s.split(':'))
        eh, em = map(int, e.split(':'))
        time = (eh - sh) * 60 + em - sm
        while len(sheet) < time:
            sheet += sheet
        if m in sheet[:time]:
            ret.append([name, time, sh])
    if not ret:
        return "(None)"
    ret.sort(key = lambda x: (x[1], -x[2]))
    return ret.pop()[0]

m = "CC"
mi = ["04:00,04:02,ZERO,ACC"] # 30번 tc - 답 (None) 
print(solution(m,mi))