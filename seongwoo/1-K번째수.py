"""
commands의 각 case마다 array를 slicing하고, 
정렬된 list에서 주어진 index의 값을 반환
"""

def solution(array, commands):
    return [sorted(array[ele[0]-1:ele[1]])[ele[2]-1] for ele in commands]