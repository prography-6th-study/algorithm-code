def solution(routes):
    routes.sort()
    answer = 0
    check = [0]*len(routes)

    for i in range(len(routes)-1, -1, -1):
        if check[i] == 0: #아직 카메라에 찍히지 않은 차
            cemara = routes[i][0] # 진입점에 카메라 설치
            answer += 1 # 카메라 댓수 증가

        for j in range(i, -1, -1):
            if check[j] == 0 and routes[j][0] <= cemara <= routes[j][1] : # 카메라가 진입점과 진출점 사이에 있으면
              check[j]=1
    return answer

solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])

"""풀이방법
-15에 사로잡혀서 -15 아니고 -18부터-13까지 다 되는거 아닌가 하고 한참 고민
어차피 최소 카메라 댓수라 상관없다는걸 깨달았다

진입 진출 지점에서 만나도 만난다고 했으니 진입점에 카메라를 두는 것으로 간주하기로 했다

뒤에서부터 진입로에 카메라를 설치한다
차량이 찍히는지 확인한다
다 찍힐 때까지 계속 추가한다


다른 풀이
def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer
이거보고 허무했다...
"""