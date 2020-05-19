"""
전화번호부의 각 element를 기준으로 전화번호부를 돌면서
시작 부분이 element와 동일한지 체크한다.
"""

def solution(phone_book):
    answer = True
    flag = False
    for i in phone_book:
        for j in phone_book:
            if i==j:
                continue
            if j[:len(i)] == i:
                answer = False
                flag = True
                break
        if flag == True:
            break
    return answer