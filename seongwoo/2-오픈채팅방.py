"""
dictionary를 만들어 놓고, record를 돌면서 {user id : nickname} 형태로 key와 value를 넣어놓음
모든 record를 확인하여 업데이트한 이후에, dictionary에 접근하면서 result 출력
"""

def solution(record):
    d = dict()
    li, ret = [], []
    for r in record:
        if r.split()[0] == 'Leave':
            r1, r2 = r.split()
        else:
            r1, r2, r3 = r.split()
        if r1 == "Enter":
            d[r2] = r3
            li.append((r2, 0))
        elif r1 == "Leave":
            li.append((r2, 1))
        else:
            d[r2] = r3
    for user, io in li:
        if io == 0:
            ret.append(d[user] + "님이 들어왔습니다.")
        else:
            ret.append(d[user] + "님이 나갔습니다.")
    return ret