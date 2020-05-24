###### 문제 설명

수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

##### 제한 조건

- 시험은 최대 10,000 문제로 구성되어있습니다.
- 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
- 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

##### 입출력 예

| answers     | return  |
| ----------- | ------- |
| [1,2,3,4,5] | [1]     |
| [1,3,2,4,2] | [1,2,3] |

##### 입출력 예 설명

입출력 예 #1

- 수포자 1은 모든 문제를 맞혔습니다.
- 수포자 2는 모든 문제를 틀렸습니다.
- 수포자 3은 모든 문제를 틀렸습니다.

따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.

입출력 예 #2

- 모든 사람이 2문제씩을 맞췄습니다.

### 내 코드

```python
import collections
def solution(answers):
    answer = []
    man1 = [1, 2, 3, 4, 5] * 2001
    man2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1251
    man3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1001
    l = len(answers)
    m1 = man1[:l]
    m2 = man2[:l]
    m3 = man3[:l]
    c1, c2, c3 = 0, 0, 0
    for idx, i in enumerate(answers):
        for jdx, j in enumerate(m1):
            if i == j and idx == jdx:
                c1 += 1
        for jdx, j in enumerate(m2):
            if i == j and idx == jdx:
                c2 += 1
        for jdx, j in enumerate(m3):
            if i == j and idx == jdx:
                c3 += 1
    answer.append(c1)
    answer.append(c2)
    answer.append(c3)
    max_num = max(answer)
    result = []
    for el in range(len(answer)):
        if max_num<=answer[el]:
            result.append(el+1)

    return result
```

- 3문제 시간초과 발생하였음.. n^2 로는 안되나 생각했다.

### 다른 사람 코드

```python
def solution(answers):
   first = [1,2,3,4,5]
   second = [2,1,2,3,2,4,2,5]
   third = [3,3,1,1,2,2,4,4,5,5]
   fc = sc = tc = 0
   for i in range(len(answers)):
       if first[i%(len(first))] == answers[i]: fc+=1
       if second[i%(len(second))] == answers[i]: sc+=1
       if third[i%(len(third))] == answers[i]: tc+=1
   MAX = max(fc, sc, tc)
   answer = []
   if MAX == fc: answer.append(1)
   if MAX == sc: answer.append(2)
   if MAX == tc: answer.append(3)
   return answer
```

### 궁굼한 점

- 나머지를 생각하게된 과정? 이 궁굼합니다~