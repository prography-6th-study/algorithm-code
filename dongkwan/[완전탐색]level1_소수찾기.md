###### 문제 설명

한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

##### 제한사항

- numbers는 길이 1 이상 7 이하인 문자열입니다.
- numbers는 0~9까지 숫자만으로 이루어져 있습니다.
- 013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

##### 입출력 예

| numbers | return |
| ------- | ------ |
| 17      | 3      |
| 011     | 2      |

##### 입출력 예 설명

예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

- 11과 011은 같은 숫자로 취급합니다.

### 내코드

```python
def solution(n):
    li = list(n)
    li.sort(reverse=True)
    n = ("".join(li))
    n = int(n)
    answer = set(range(2,n+1))
    for i in range(2,n+1):
        if i in answer:
            answer-=set(range(i*2, n+1, i))
    for el in answer:
        kk = map(list(str,el))
        print(kk)
    print(li)
    for i in range(len(answer)):
        for j in li:
            pass
    return len(answer)
```

### 다른사람 코드

```python
def solution(n):
    answer = [False, False]+[True]*(n-1)
    for i in range(int(n**0.5)+1):
        if answer[i] == True:
            for j in range(2*i, n+1, i):
                answer[j] = False
    return sum(answer)
```

### 궁굼한 점

- 왜 다들 소수만 찾고 끝이지? 수가 있는지 비교해보는건 어떻게 찾는지 궁굼.