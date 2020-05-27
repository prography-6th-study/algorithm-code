"""
원래 풀려고 했던 방법은 sort의 key값에 (장르순위, 장르내 순위, 고유번호index)를 한꺼번에 넣은 후에 
전체적으로 하나의 배열로 만들어서 각 장르에서 2개씩 빼려고 했는데, 장르에 속한 곡이 하나라면 하나만 빼라는 조건을 처리하기가 생각보다 까다로웠다.
따라서 장르별로 따로 나눠서 정렬 후 슬라이싱 처리하는 방법으로 바꾸게 되었다.
dict.get() 메소드에 대해서 알게 되었는데, dict[key]로 접근하면 키가 없을 경우에 Error가 생기는 반면,
dict.get(key)로 접근하면 키가 dictionary에 없을 경우 None을 반환하여 유용하게 사용 가능하다.
"""

def solution(genres, plays):
    answer = []
    d = dict()
    play_d = dict()
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        play_d[genre] = play_d.get(genre, 0) + play
        d[genre] = d.get(genre, []) + [(play, i)]
    for (genre, _) in sorted(play_d.items(), key=lambda x: x[1], reverse=True):
        d[genre] = sorted(d[genre], key=lambda x: (-x[0], x[1]))
        answer += [idx for (_, idx) in d[genre][:2]]
    return answer


g = ["classic", "pop", "classic", "classic", "pop"]
p = [500, 600, 150, 800, 2500]

g2= ["classic", "pop", "classic", "pop", "classic", "classic"]
p2 = [400, 600, 150, 2500, 500, 500]

g3= ["classic", "pop", "classic"]
p3 = [400, 600, 150]

print(solution(g2,p2))