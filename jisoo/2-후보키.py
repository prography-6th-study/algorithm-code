from itertools import combinations

import pytest


def get_combination_index_relation(relation, combination):
    temp = []
    count = 0
    for r in relation:
        r_temp = []
        for c in combination:
            r_temp.append(r[c])
        temp.append(r_temp)
        count += 1
    if count == len(set(map(tuple, temp))):
        return True
    return False


def check_minimality(answer, combination):
    for a in answer:
        if len(a) == len(combination):
            continue
        check = 0
        for c in combination:
            if c in a:
                check += 1
        if check == len(a):
            return False
    return True


def solution(relation):
    index = [i for i in range(len(relation[0]))]
    answer = []
    combination = []

    for increase in range(1, len(relation[0])+1):
        combination.extend(list(combinations(index, increase)))

    for c in combination:
        if get_combination_index_relation(relation, c):
            if check_minimality(answer, c):
                answer.append(c)
    print(answer)
    return len(answer)


@pytest.mark.parametrize("relation, expected", [
    ([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]], 2),
    ([['a', 'b', 'c'], [1, 'b', 'c'], ['a', 'b', 4], ['a', 5, 'c']], 1),
    ([['a', 1, 4], [2, 1, 5], ['a', 2, 4]], 2),
    ([['b', 2, 'a', 'a', 'b'], ['b', 2, 7, 1, 'b'], [1, 0, 'a', 'a', 8], [7, 5, 'a', 'a', 9], [3, 0, 'a', 'f', 9]], 5)

])
def test_simple(relation, expected):
    assert solution(relation) == expected

"""
[ 풀이 방법 ]
- 
"""