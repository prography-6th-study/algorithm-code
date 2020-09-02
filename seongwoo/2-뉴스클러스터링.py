"""
문제를 꼼꼼히 읽었으면 실수가 줄었을듯!
집합 단어만 보고 set으로 접근했는데 중복을 허용하는 다중집합이었다.

중간에 테스트케이스 4, 7, 9, 10, 11 이 계속 틀렸었는데, 해당 케이스는 아래와 같았다.
교집합을 구하는 것에서 개수를 셀 때 동일한 원소에 접근하지 않도록,
교집합 cnt가 올라갈 때마다 해당 원소를 탐색 대상 리스트에서 삭제해야했다.
"""


def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    m1, m2 = [], []

    for i in range(len(str1) - 1):
        if 65 <= ord(str1[i]) <= 90 and 65 <= ord(str1[i + 1]) <= 90:
            m1.append(str1[i] + str1[i + 1])
    for i in range(len(str2) - 1):
        if 65 <= ord(str2[i]) <= 90 and 65 <= ord(str2[i + 1]) <= 90:
            m2.append(str2[i] + str2[i + 1])
    
    intersect = 0
    tmp = m2[:]
    for ele in m1:
        if ele in m2:
            m2.remove(ele)
            intersect += 1
    m2 = tmp
    union = len(m1) + len(m2)  - intersect 
    if not union:
        return 65536
    similar = intersect / union
    return int(similar * 65536)

print(solution('FRANCE', 'french'))