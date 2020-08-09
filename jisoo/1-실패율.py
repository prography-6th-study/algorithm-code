import pytest
from collections import Counter


def solution(N, stages):
    people = len(stages)
    stages.sort()
    stages_count = {}
    stages = dict(Counter(stages))
    # dict 형태로 각 레벨마다 통과 못한 사람 수 세주기
    for idx in range(1, N+1):
        stages_count[idx] = stages.get(idx, 0)

    # 실패율 계산
    failure_rates = {}
    for stage, count in stages_count.items():
        if people==0 and count==0:
            failure_rates[stage] = 0
            continue
        failure_rate = count/people
        people -= count
        failure_rates[stage] = failure_rate

    # 정렬하고 answer에 넣어주기
    failure_rates = dict(sorted(failure_rates.items(), key=lambda x: (-x[1], x[0])))
    answer = []
    for failure_rate in failure_rates.keys():
        answer.append(failure_rate)
    return answer


@pytest.mark.parametrize("N, stages, expected", [
    (5, [2, 1, 2, 6, 2, 4, 3, 3], [3, 4, 2, 1, 5]),
    (4, [4, 4, 4, 4, 4], [4, 1, 2, 3]),
    (4, [5, 5, 5, 5, 4], [4, 1, 2, 3])
])
def test_simple(N, stages, expected):
    assert solution(N, stages) == expected

"""
[ 풀이 방법 ]
- 
"""