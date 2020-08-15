from collections import deque

def solution(skill, skill_trees):
    cnt = len(skill_trees)  # 가능한 스킬트리 개수 (최대로 설정)
    for skill_tree in skill_trees:
        temp = deque(skill)  # 선행 스킬트리 초기화
        for s in skill_tree:
            # 순서가 있는 스킬들만 검사
            if s in temp:
                # s가 선행 스킬 순서의 맨 앞에 있는 값이면 해당 선행 스킬을 삭제
                if temp[0] == s:
                    temp.popleft()
                # s가 선행 스킬인데 순서를 지키지 않으면 cnt를 하나 빼주고 검사를 종료
                else:
                    cnt -= 1
                    break
    return cnt


# test
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))