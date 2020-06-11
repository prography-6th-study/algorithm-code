from itertools import permutations
def play(x,y):
    x = list(x)
    y = list(y)
    s = 0 # 스트라이크 갯수
    b = 0 # 볼 갯수
    for i in range(3):
        if x[i] in y:
            if y.index(x[i]) == i: s+=1 # 숫자, 위치 둘 다 맞을 때
            else: b+=1 # 숫자는 맞지만, 위치가 틀렸을 때는 볼
    return [s, b]

def solution(baseball):
    v = list(map(lambda x: str(x[0]), baseball)) # 예상한 숫자
    r = list(map(lambda x: [x[1], x[2]], baseball)) #각 예상 숫자에 대한 스트라이크, 볼 수

    #lst 가능한 모든 숫자 조합
    lst = list(permutations(range(1,10), 3))
    # ['1','2','3'] 요런식으로 나타내기
    lst = list(map(lambda x: list(map(str, x)), lst))

    answer = 0

    for x in lst:
        # lst에 있는 조합 중 스트라이크 볼 갯수가 r 처럼 나온 숫자면 answer+1
        if [play(x,y) for y in v] == r: answer+=1 
    return answer

solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]])