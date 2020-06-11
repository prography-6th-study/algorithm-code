###### 문제 설명

어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

##### 제한 조건

- number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
- k는 1 이상 `number의 자릿수` 미만인 자연수입니다.

##### 입출력 예

| number     | k    | return |
| ---------- | ---- | ------ |
| 1924       | 2    | 94     |
| 1231234    | 3    | 3234   |
| 4177252841 | 4    | 775841 |

[출처](http://hsin.hr/coci/archive/2011_2012/contest4_tasks.pdf)



내 풀이 1

```python
def solution(number, k):
    if len(number) == 1 and k == 1:
        return "0"
    li = list(number)
    li.sort(reverse=True)
    answer = "".join(li[:-k])

    return answer
```

- 예외 처리하였음
- 리스트화 시키고 내림차순 정렬시키고, 두개 빼주면 된다고 생각했었다.
- 틀림

- 이유 : 문제 지문 잘못 이해함. 리스트를 섞으면 안된다.



내 풀이 2

```PYTHON
from itertools import combinations

def solution(number, k):
    final = []
    if len(number) == 1 and k == 1:
        return "0"
    li = list(number)
    tmp_list = [_ for _ in range(0,len(li))]
    combi = list(combinations(tmp_list, k))
    for i in combi:
        tmp = li.copy()
        visited = [True]*len(li)
        for j in i:
            visited[j] = False
        answer = ""
        for j in range(len(visited)):
            if visited[j] == True:
                answer += tmp[j]
        final.append(answer)
    final.sort()
    return final[-1]
```

- visited 배열을 선정하였습니다.
- 콤비네이션으로 나온 인덱스 결과를 바탕으로 True 처리 되었다면 추가해주는 방식을 사용하였습니다.
- 그 후 숫자를 모두 리스트에 담아 그중 가장 큰 수를 반환하도록 만들었습니다.
- 틀림

- 완전탐색은 시간초과가 나온다는 것을 알게 되었습니다.



타인의 풀이를 이해하자

```python
def solution(number,k):
    alist = [number[0]]
    for num in number[1:]:
        # 들어오는 숫자가 alist 맨 뒤 숫자보다 클 때. 바꿔치기한다.
        while len(alist) > 0 and alist[-1] < num and k > 0:
            k-=1
            alist.pop()
        alist.append(num)
    if k!=0:
        alist = alist[:-k]
    return "".join(alist)
```

