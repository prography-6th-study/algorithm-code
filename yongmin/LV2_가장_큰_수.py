from functools import cmp_to_key

def compare(x, y):
    s1 = x + y  # 문자열 결합
    s2 = y + x

    if int(s1) > int(s2):  # int로 바꾼 후 비교
        return -1
    elif int(s1) < int(s2):
        return 1
    elif int(s1) == int(s2):
        return 0


def solution(numbers):
    str_list = [str(number) for number in numbers]
    sorted_list = sorted(str_list, key=cmp_to_key(compare))

    answer = "".join(map(str, sorted_list))
    return answer if answer[0] != '0' else '0'


#test
print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))