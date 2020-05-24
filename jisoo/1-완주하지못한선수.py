import pytest
from collections import Counter


def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    # 메모리 낭비를 줄이기 위해 dict_keys 객체를 돌려준다.
    # 반환 값으로 리스트가 필요한 경우에는 list(a.keys())를 사용하면 된다.
    return list(answer.keys())[0]


@pytest.mark.parametrize("participant, completion, expected", [
    (["eden", "kiki", "eden"], ["eden", "kiki"], "eden"),
    (["marina", "josipa", "nikola", "vinko", "filipa"],
        ["josipa", "filipa", 'marina', 'nikola'], 'vinko')
])
def test_simple(participant, completion, expected):
    assert solution(participant, completion) == expected
