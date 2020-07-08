def solution(record):
    user = {}  # id : 닉네임
    log = []  # (id, 출입)
    for r in record:
        temp = r.split(" ")
        # Enter: 유저 갱신, log 추가
        if temp[0] == "Enter":
            user[temp[1]] = temp[2]
            log.append((temp[1], temp[0]))
        # Leave: log 추가 (닉네임 변경 없음)
        elif temp[0] == "Leave":
            log.append((temp[1], temp[0]))
        # Change: 유저 갱신 (기록 남지 않음)
        else:
            user[temp[1]] = temp[2]

    result = []
    for id, action in log:
        message = ""
        if action == "Enter":
            message = "{}님이 들어왔습니다.".format(user[id])
        elif action == "Leave":
            message = "{}님이 나갔습니다.".format(user[id])
        result.append(message)

    return result


# test
print(solution(["Enter uid1234 Muzi",
                "Enter uid4567 Prodo",
                "Leave uid1234",
                "Enter uid1234 Prodo",
                "Change uid4567 Ryan"]))