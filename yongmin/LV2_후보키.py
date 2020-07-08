from itertools import combinations

def solution(relation):
    col_len = len(relation[0])  # 칼럼 개수
    col_indexes = list(range(col_len))  # 칼럼의 인덱스 리스트
    check_list = []  # 칼럼 인덱스 조합들을 담을 리스트
    answer_list = []

    # 조합 만들기
    for i in range(1, col_len+1):
        c = combinations(col_indexes, i)
        check_list.extend(c)  # # [(0,), (1,), (2,),,,

    # 유일성 만족하는 조합 찾기
    for cols in check_list:
        values = []
        # 릴레이션 길이만큼 반복
        for row in range(0, len(relation)):
            temp_list = []
            # 하나의 row에 해당하는 후보키 속성들을 추가
            for col in cols:
                temp_list.append(relation[row][col])
            values.append(tuple(temp_list))
        # 유일성 만족하는지 체크 (중복된 값이 없어야 함)
        if len(set(values)) == len(relation):
            answer_list.append(cols)

    # 최소성을 만족하는 조합 찾기
    answer_set = set(answer_list)
    for i in range(len(answer_list)-1):
        for j in range(i+1, len(answer_list)):
            # A 조합과 A 교집합 B가 같은 경우 : 최소성을 만족하지 못함
            if set(answer_list[i]) == set(answer_list[i]) & set(answer_list[j]):
                answer_set.discard(answer_list[j])

    return len(answer_set)


# test
print(solution([["100", "ryan", "music", "2"],
                ["200", "apeach", "math", "2"],
                ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"],
                ["500", "muzi", "music", "3"],
                ["600", "apeach", "music", "2"]]))