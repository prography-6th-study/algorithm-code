def solution(s):
    tuples = {}  # 원소의 개수 : {원소들..}
    # {{ }} 는 제외하고 },{ 구분해서 split ['2', '2,1', '2,1,3', '2,1,3,4']
    splited = s[2:-2].split("},{")

    # split한 리스트의 원소들을 , 구분해서 split 한 후
    # 이 값을 tuples에 개수 : {a, b, c,,,} 형태로 저장
    # {1: {'2'}, 2: {'1', '2'}, 3: {'1', '3', '2'}, 4: {'1', '3', '4', '2'}}
    for v in splited:
        temp = v.split(",")
        tuples[len(temp)] = set(temp)

    # tuples에 i+1 set와 i set의 차집합을 구해서 정답을 찾아낸다
    answer = [list(tuples[1])[0]]
    for i in range(1, len(tuples)):
        attr = (tuples[i+1] - tuples[i]).pop()
        answer.append(attr)

    return list(map(int, answer))



# test
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))