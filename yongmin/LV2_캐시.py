def solution(cacheSize, cities):
    answer = 0

    # 캐시의 크기가 0인 경우
    if cacheSize == 0:
        answer = len(cities) * 5
        return answer

    cache = []
    for s in cities:
        city = s.lower()  # 대소문자 구분하지 않으므로 소문자로 통일
        # 현재 도시가 캐시 안에 있는 경우
        if city in cache:
            answer += 1  # 실행시간 +1
            cache.remove(city)  # 캐시에서 해당 도시를 삭제
            cache.append(city)  # 캐시에 해당 도시를 넣어줌 (가장 최근에 들어간 데이터)
        # 현재 도시가 캐시 안에 없는 경우
        else:
            answer += 5  # 실행시간 +5
            if len(cache) >= cacheSize:  # 캐시가 꽉 찬 경우
                cache.pop(0)  # 가장 오래된 데이터를 삭제
            cache.append(city)  # 캐시에 해당 도시를 넣어줌
    return answer


# test
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))