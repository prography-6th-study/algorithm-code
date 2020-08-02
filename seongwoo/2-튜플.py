"""
python에서는 eval()을 쓰는 것을 별로 권장하지 않는다고 했는데, string to array 방식이 떠오르는 게 eval 밖에 없었다..
string을 2중 배열로 변환한 뒤, 원소길이가 작은 것부터 오름차순으로 정렬하고,
해당 list를 돌면서 추가되는 원소를 결과값에 하나씩 append하였다.
"""

def solution(s):
    ret = []
    s = s.replace('{','[').replace('}',']')
    sorted_s = sorted(eval(s), key=lambda x: len(x))
    length = len(sorted_s)
    for idx, i in enumerate(sorted_s):
        if idx == 0:
            ret.append(i[0])
            continue
        ele = set(i) - set(sorted_s[idx - 1])
        ret.append(list(ele)[0])
    return ret


s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s2 ="{{1,2,3},{2,1},{1,2,4,3},{2}}"	
print(solution(s2))