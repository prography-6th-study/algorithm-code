import pytest


def solution(n, words):
    result = [0, 0]
    used_words = []

    for idx, word in enumerate(words):
        if idx == 0:
            used_words.append(word)
        elif word[0] == words[idx-1][-1] and word not in used_words:
            used_words.append(word)
        else:
            result = [idx % n + 1, idx // n + 1]
            break
    return result


@pytest.mark.parametrize("n, words, expected", [
    (3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"], [3, 3]),
    (5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"], [0, 0]),
    (2, ["hello", "one", "even", "never", "now", "world", "draw"], [1, 3])
])
def test_simple(n, words, expected):
    assert solution(n, words) == expected

"""
[ 풀이 방법 ]
- for 문 안에서 한번에 체크하는게 더 좋
"""