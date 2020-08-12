"""
각 스킬트리 중에서 skill에 해당하는 string만 빼서
해당 string의 길이만큼 skill을 인덱싱한 것과 string이 일치하면 cnt를 늘려주었음
"""

def solution(skill, skill_trees):
    cnt = 0
    for tree in skill_trees:
        tmp = ""
        for t in tree:
            if t in skill:
                tmp += t
        if skill[:len(tmp)] == tmp:
            cnt += 1
    return cnt

s = "CBD"
t = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(s,t))