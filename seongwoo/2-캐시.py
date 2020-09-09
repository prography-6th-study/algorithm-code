def solution(cacheSize, cities):
    cities = [c.lower() for c in cities]
    cache = dict()
    time = 0
    if not cacheSize:
        return len(cities) * 5
    for city in cities:
        s = sorted(cache.items(), key=lambda x: x[1], reverse=True)
        for c in cache:
            cache[c] -= 1
        if not cache:
            cache[city] = 0
            time += 5
        elif city in cache:
            cache[city]  = 0 
            time += 1
        elif len(cache) < cacheSize:
            cache[city] = 0
            time += 5
        else:
            del cache[s.pop()[0]]
            cache[city] = 0
            time += 5
    return time

print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(5, ["SEOUL", "SEOUL", "SEOUL"]))