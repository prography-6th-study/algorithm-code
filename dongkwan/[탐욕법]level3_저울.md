###### 문제 설명

하나의 양팔 저울을 이용하여 물건의 무게를 측정하려고 합니다. 이 저울의 양팔의 끝에는 물건이나 추를 올려놓는 접시가 달려 있고, 양팔의 길이는 같습니다. 또한, 저울의 한쪽에는 저울추들만 놓을 수 있고, 다른 쪽에는 무게를 측정하려는 물건만 올려놓을 수 있습니다.

![image0.png]([탐욕법]level3_저울/img/f4abf5ff-1956-4e49-bd4a-d3d24619bbf0.png)

저울추가 담긴 배열 weight가 매개변수로 주어질 때, 이 추들로 측정할 수 없는 양의 정수 무게 중 최솟값을 return 하도록 solution 함수를 작성해주세요.

예를 들어, 무게가 각각 [3, 1, 6, 2, 7, 30, 1]인 7개의 저울추를 주어졌을 때, 이 추들로 측정할 수 없는 양의 정수 무게 중 최솟값은 21입니다.

##### 제한 사항

- 저울추의 개수는 1개 이상 10,000개 이하입니다.
- 각 추의 무게는 1 이상 1,000,000 이하입니다.

##### 입출력 예

| weight                 | return |
| ---------------------- | ------ |
| [3, 1, 6, 2, 7, 30, 1] | 21     |

##### 입출력 예 설명

문제에 나온 예와 같습니다.

[출처](https://www.digitalculture.or.kr/koi/selectOlymPiadDissentList.do)

## 코드

```python
def solution(weights):
    weights.sort()
    temp = weights.pop(0)
    for i in range(len(weights)):
        if temp + 1 < weights[i]:
            break
        else:
            temp += weights[i]

    return temp + 1

weight = [3, 1, 6, 2, 7, 30, 1]

print(solution(weight))
```

- 탐욕법 == 정렬 후 계산.
- 부분합은 무조건 그 수까지는 어떻게든 만들 수 있다는 생각이 필요하다.