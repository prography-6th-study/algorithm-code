###### 문제 설명

조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

```
▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동
```

예를 들어 아래의 방법으로 JAZ를 만들 수 있습니다.

```
- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
```

만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

##### 제한 사항

- name은 알파벳 대문자로만 이루어져 있습니다.
- name의 길이는 1 이상 20 이하입니다.

##### 입출력 예

| name   | return |
| ------ | ------ |
| JEROEN | 56     |
| JAN    | 23     |

[출처](https://commissies.ch.tudelft.nl/chipcie/archief/2010/nwerc/nwerc2010.pdf)

※ 공지 - 2019년 2월 28일 테스트케이스가 추가되었습니다.



### 다른 사람 코드

```python
def solution(name):
    # 1. 알파벳을 맞추는 최소 횟수를 저장하는 배열 m을 만듭니다.
    m = [ min(ord(c) - ord("A"), ord("Z") - ord(c) + 1)  for c in name  ]
    answer = 0
    where = 0

    # 2. 위치 where를 0부터 시작해서, 다음을 반복합니다.
    while True:
        # 1. m[where]를 answer에 더합니다
        answer += m[where]
        # 2. m[where]를 0으로 만듭니다.
        m[where] = 0
        
        # 3. 만약, 현재 m이 모두 0이라면, 반복을 멈춥니다.
        if sum(m) == 0:
            break
        
        # 4. 3이 만족하지 않을 때, left, right를 1로 만듭니다.
        left, right = (1, 1)
        
        # 5. m[where-left] <= 0일 때까지, left를 1씩 증가시킵니다.
        while m[where - left] <= 0:
            left += 1
        # 6. m[where+right] <= 0일 때까지 right를 1씩 증가시킵니다.            
        while m[where + right] <= 0:
            right += 1
        
        # 7. left, right를 비교합니다.
        # 7-1. left < right 라면, answer에 left를 더하고, where에 -left를 더합니다.
        # 7-2. 반대라면, answer에 right를 더하고 where에 right를 더합니다.
        answer += left if left < right else right
        where += -left if left < right else right
            
    return answer
```

```python
def solution(name):
    answer = 0
    name=list(name)
    index=0
    while(True):
        right=1
        left=1
        if name[index] != 'A': 
            updown = min(ord(name[index])-ord('A'),(ord('Z')-ord(name[index])+1))
            answer += updown
        name[index] = 'A'
        if name == ["A"]*len(name): break
        for i in range(1,len(name)):
            if name[index+i]=="A": right+=1
            else: break
        for i in range(1,len(name)):
            if name[index-i]=="A": left+=1
            else: break
        if right>left:
            answer+=left
            index-=left
        else:
            answer+=right
            index+=right
    return answer
```

### 알게된 것

## ord

ord(c)는 문자의 아스키 코드 값을 돌려주는 함수이다.

> ※ ord 함수는 chr 함수와 반대이다.

```
>>> ord('a')
97
>>> ord('0')
48
```

