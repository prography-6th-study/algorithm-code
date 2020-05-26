def solution(genres, plays):
    answer = []

    total = {}  # 장르별 총합
    songs = {}  # 장르별 (재생횟수, 인덱스)

    # 딕셔너리 초기화
    for i in range(len(genres)):
        try:
            total[genres[i]] += plays[i]
            songs[genres[i]].append((plays[i], i))
        except KeyError:
            total[genres[i]] = plays[i]
            songs[genres[i]] = [(plays[i], i)]

    # 장르별 재생횟수 내림차순으로 정렬
    sorted_genre = sorted(total.items(), key=lambda x: x[1], reverse=True)

    for (genre, total_play) in sorted_genre:
        # 노래별 재생횟수 내림차순, 인덱스 오름차순 정렬
        songs[genre] = sorted(songs[genre], key=lambda x: (-x[0], x[1]))
        # 각 장르별 2개의 index를 추가
        answer += [ i for (play, i) in songs[genre][:2] ]

    return answer




# test
print(solution(["classic", "pop", "classic", "classic", "pop"],
               [500, 600, 150, 800, 2500]))