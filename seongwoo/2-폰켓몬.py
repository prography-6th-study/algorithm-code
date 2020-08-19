"""
처음에는 len(max(map(set, combinations(nums, len(nums) // 2)), key = lambda x: len(x))) 이렇게
조합으로 접근을 했는데 시간초과가 났고, 경우의 수를 나누어서 다시 접근하고 통과하였다.
중복을 제거했을 때 해당 갯수가 N/2 마리보다 작다면 해당 값을 리턴하고, 아닌 경우에는 N/2 을 리턴.
문제를 꼼꼼히 읽었다면 시행착오 없이 풀 수 있는 문제였다.
"""


def solution(nums):
    if len(set(nums)) < len(nums) // 2:
        return len(set(nums))
    else:
        return len(nums) // 2

n = [3,3,3,2,2,4]
print(solution(n))