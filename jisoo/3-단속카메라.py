import pytest


def solution(routes):
    routes.sort()
    answer = 1
    camera = routes[0][1]
    for start, end in routes:
        # 진출 지점이 카메라보다 앞에 있는 경우 카메라 위치 갱신
        if end <= camera:
            camera = end
        # 진입 지점이 카메라 밖에 있는 경우 카메라를 새로 설치해 준다.
        elif start > camera:
            answer += 1
            camera = end
    return answer

@pytest.mark.parametrize("routes, expected", [
    ([[-20, 15], [-14, -5], [-18, -13], [-5, -3]], 2)
])
def test_simple(routes, expected):
    assert solution(routes) == expected

"""
[ 풀이 방법 ]
- 차들이 겹치지 않는 부분의 개수를 구하면 될 것 같았다.
- for문 2번 돌면서 겹치는 것을 확인..?
해봤는데 틀렸다... 테스트케이스는 통과하지만 다른건 안됨
결국 인터넷을 찾아봤다.


- 첫 카메라 설치 위치는 가장 빨리 고속도로를 진입한 차의 진출 지점
 
반복문을 돌면서 아래 내용을 수행
- i번째 차량의 진출 지점이 최근 설치한 카메라 위치 이전에 있을 경우, 카메라 위치를 i번째 차량의 진출 지점으로 갱신
- i번째 차량이 최근 설치한 카메라를 만나지 않을 경우, 새로운 카메라 설치 후 카메라 위치를 i번째 차량의 진출 지점으로 갱신


이런걸 어떻게 생각하나 싶다... 아직 멀었다 ㅜㅅㅜ
"""