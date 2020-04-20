###### 문제 설명

0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

##### 제한 사항

- numbers의 길이는 1 이상 100,000 이하입니다.
- numbers의 원소는 0 이상 1,000 이하입니다.
- 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

##### 입출력 예

| numbers           | return  |
| ----------------- | ------- |
| [6, 10, 2]        | 6210    |
| [3, 30, 34, 5, 9] | 9534330 |

### 내 코드

```python
def solution(numbers):
    answer = ''
    from itertools import permutations
    perm = permutations(numbers)
    result = []
    for p in perm:
        hi = "".join(map(str,p))
        result.append(hi)
    answer = max(result)
    return answer
```

- 모든 경우의 수가 시간초과 나왔다.
- 다른 방식이 생각 안나서 fail.

### 다른 사람 코드

```python
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    # print(numbers)
    return str(int(''.join(numbers)))
```

- 자릿수를 맞춰준다는데 뭔소린지 모르겠음.

### 알게된 것

- lambda()

  g = lambda x:x**2

  g(8)을 프린트 해주면 64가 나옵니다. 람다는 요런식으로 써줍니다.