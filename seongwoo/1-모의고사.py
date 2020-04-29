def solution(answers):
    length = len(answers)
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    one_li, two_li, three_li = [], [], []

    for _ in range(length//5): one_li.extend(one)
    one_li.extend(one[:length%5])
    for _ in range(length//8): two_li.extend(two)
    two_li.extend(two[:length%8])
    for _ in range(length//10): three_li.extend(three)
    three_li.extend(three[:length%10])

    cnt_one, cnt_two, cnt_three = 0, 0, 0
    for a, b in zip(one_li,answers):
        if a == b: cnt_one += 1
    for a, b in zip(two_li,answers):
        if a == b: cnt_two += 1
    for a, b in zip(three_li,answers):
        if a == b: cnt_three += 1
    
    cnt_li = [cnt_one, cnt_two, cnt_three]
    ret = []
    for idx, i in enumerate(cnt_li):
        if i == max(cnt_li):
            ret.append(idx+1)
    return ret