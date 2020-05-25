def solution(genres, plays):
    answer = []  
    playTime = {}
    dic = {}
    for i in range(len(genres)):
        genre = genres[i]
        time = plays[i]

        playTime[genre] = playTime.get(genre, 0) + time
        dic[genre] = dic.get(genre, []) + [(time, i)]
    
    genreSorted = sorted(playTime.items(), key=lambda x:x[1] , reverse=True)

    for (genre, totalPlay) in genreSorted:
        dic[genre] = sorted(dic[genre], key=lambda x: (-x[0],x[1]))
        answer += [inx for (play,inx) in dic[genre][:2]]

    return answer