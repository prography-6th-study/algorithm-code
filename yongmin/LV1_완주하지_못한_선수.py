from collections import Counter

def solution(p, c):
    p_count = Counter(p)
    c_count = Counter(c)
    person = p_count - c_count
    return list(person.keys())[0]

# test
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))