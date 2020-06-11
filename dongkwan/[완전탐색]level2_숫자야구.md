###### 문제 설명

숫자 야구 게임이란 2명이 서로가 생각한 숫자를 맞추는 게임입니다. [게임해보기](https://scratch.mit.edu/projects/131352991/)

각자 서로 다른 1~9까지 3자리 임의의 숫자를 정한 뒤 서로에게 3자리의 숫자를 불러서 결과를 확인합니다. 그리고 그 결과를 토대로 상대가 정한 숫자를 예상한 뒤 맞힙니다.

```
* 숫자는 맞지만, 위치가 틀렸을 때는 볼
* 숫자와 위치가 모두 맞을 때는 스트라이크
* 숫자와 위치가 모두 틀렸을 때는 아웃
```

예를 들어, 아래의 경우가 있으면

```
A : 123
B : 1스트라이크 1볼.
A : 356
B : 1스트라이크 0볼.
A : 327
B : 2스트라이크 0볼.
A : 489
B : 0스트라이크 1볼.
```

이때 가능한 답은 324와 328 두 가지입니다.

질문한 세 자리의 수, 스트라이크의 수, 볼의 수를 담은 2차원 배열 baseball이 매개변수로 주어질 때, 가능한 답의 개수를 return 하도록 solution 함수를 작성해주세요.

##### 제한사항

- 질문의 수는 1 이상 100 이하의 자연수입니다.
- baseball의 각 행은 [세 자리의 수, 스트라이크의 수, 볼의 수] 를 담고 있습니다.

##### 입출력 예

| baseball                                             | return |
| ---------------------------------------------------- | ------ |
| [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]] | 2      |

##### 입출력 예 설명

문제에 나온 예와 같습니다.

[출처](https://www.digitalculture.or.kr/koi/selectOlymPiadDissentList.do)



- 모르겠다.

```python
import itertools
def solution(baseball):
    answer = 0
    num_list = list(map("".join, (itertools.permutations(['1','2','3','4','5','6','7','8','9'], 3))))
    for i in baseball:
        for j in num_list[:]:
            if not(sb(j,i)):
                num_list.remove(j)
    return len(num_list)

def sb(number,i):
    n = list(number)
    o = list(str(i[0]))
    s,b = 0,0
    for x in range(3):
       if n[x] == o[x]:
           s+=1
       elif o[x] in n:
           b+=1
    if s == i[1] and b == i[2]:
        return True
    return False
```

- 모든 경우의 수를 다 만들어놓고 하나씩 없애주고 남는 것의 길이를 잰다.