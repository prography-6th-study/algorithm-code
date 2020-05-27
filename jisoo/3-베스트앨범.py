import pytest


def solution(genres, plays):
    genre = {}
    sum = {}
    for idx, key in enumerate(genres):
        if key in genre:
            genre[key].append([-plays[idx], idx])
            sum[key] += plays[idx]
        else:
            genre[key] = [[-plays[idx], idx]]
            sum[key] = plays[idx]
    # - 로 값을 넣어준 이유는 idx가 작은 값이 앞으로 오게 정렬되라고

    # 장르 안의 값들 정렬
    for k, v in genre.items():
        v.sort()
    print(genre)
    

    # 장르들 합이 큰 순서대로 정렬
    genre = sorted(genre.items(), key=lambda k: sum[k[0]], reverse=True)

    # 정답 배열에 넣어주기
    answer = []
    for k, value in genre:
        answer += [v[1] for v in value[:2]]
    return answer


@pytest.mark.parametrize("genres, plays, expected", [
    (["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500], [4, 1, 3, 0]),
    (["classic", "pop", "classic", "classic", "pop"], [500, 600, 500, 800, 900], [3, 0, 4, 1])
])
def test_simple(genres, plays, expected):
    assert solution(genres, plays) == expected


"""
[ 풀이방법 ]
    - 장르에 따라 곡을 나눈다
    - 그 안에서 곡 횟수로 정렬하고
    - 원래 인덱스를 넣어준다
"""