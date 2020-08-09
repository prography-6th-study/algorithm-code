import pytest


def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        check = []
        for one_skill in skill_tree:
            if one_skill in skill:
                check.append(one_skill)
        flag = True
        for c, s in zip(check, skill):
            if c != s:
                flag = False
                break
        if flag:
            answer += 1
    return answer


@pytest.mark.parametrize("skill, skill_trees, expected", [
    ("CBD", ["BACDE", "CBADF", "AECB", "BDA"], 2)
])
def test_simple(skill, skill_trees, expected):
    assert solution(skill, skill_trees) == expected

"""
[ 풀이 방법 ]
- check 라는 배열에 skill안에 있는 문자열을 만나면 넣어준다.
- check 배열이 skill과 동일한 순서를 가지는지 본다
"""