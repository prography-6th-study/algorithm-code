def solution(routes):
    routes.sort()  # 진입점 기준으로 정렬
    standard = routes[0][1]  # 기준값 초기화
    routes.pop(0)
    answer = 1  # 필요 단속카메라 수

    for route in routes:
        # 현재 경로의 진입점이 기준값(이전 경로의 도착점)보다 작거나 같으면 포함 관계
        if route[0] <= standard:
            # 기준값을 현재 경로의 도착점과 기준값 중 작은 값으로 재설정
            standard = min(route[1], standard)
        # 포함되지 않으면 새로운 경로 시작
        else:
            standard = route[1]  # 기준점을 현재 경로의 도착점으로
            answer += 1  # 단속카메라 +1

    return answer


# test
print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))