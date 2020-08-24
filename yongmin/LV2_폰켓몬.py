def solution(nums):
    x = len(nums) // 2  # 가져갈 수 있는 폰켓몬 갯수
    nums = set(nums)  # set 으로 중복 값 제거

    # nums의 갯수가 x보다 크거나 같으면 x
    if len(nums) >= x:
        return x
    # 아니면 nums의 길이가 최대로 가져갈 수 있는 폰켓몬 갯수
    else:
        return len(nums)


# test
print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))