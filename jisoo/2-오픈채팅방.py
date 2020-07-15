import pytest


def solution(record):
    name = dict()
    for r in record:
        temp = r.split(" ")
        if temp[0] in ['Enter', 'Change']:
            name[temp[1]] = temp[2]

    answer = []
    for r in record:
        temp = r.split(" ")
        if temp[0] == 'Enter':
            answer.append(name[temp[1]]+'님이 들어왔습니다.')
        elif temp[0] == 'Leave':
            answer.append(name[temp[1]]+'님이 나갔습니다.')

    return answer
    


@pytest.mark.parametrize("record, expected", [
    (["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"],
     ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."])
])
def test_simple(record, expected):
    assert solution(record) == expected

"""
[ 풀이 방법 ]
- 해시로 하면 될 것 같았다. uid 키로 하고 enter, change가 들어오면 이름을 바꿔준다?
"""