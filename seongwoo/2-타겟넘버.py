"""
dfs를 이용해서 구현.
이진트리에서 자식 노드에 numbers 배열의 각 index에 해당하는 
element와 element*(-1)의 값이 각각 양쪽으로 연결된다고 생각하고 접근하였음.

+ 추가적으로 python에서 global과 nonlocal의 차이에 대해 검색해보는 계기가 되었음. 
프로그래머스는 기본적으로 solution 함수에 작성하도록 되어 있기 때문에, 
함수 내 함수를 정의할 때 지역변수가 아님을 알리기 위해 nonlocal로 정의해주는 방법을 많이 사용하는 것 같음.
하지만 개인적으로는 함수를 밖으로 빼는 것과 global 변수 정의를 선호하기 때문에 이 방법을 사용함.
"""

def op(nums, t, _sum, idx):
    global cnt
    if idx < len(nums):
        op(nums, t, _sum + nums[idx], idx + 1)
        op(nums, t, _sum - nums[idx], idx + 1)
    elif _sum == t:
        cnt += 1
        return

cnt = 0
def solution(numbers, target):
    op(numbers, target, 0, 0)
    return cnt