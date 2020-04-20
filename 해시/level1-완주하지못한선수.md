# 완주하지 못한 선수

###### 문제 설명

수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

##### 제한사항

- 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
- completion의 길이는 participant의 길이보다 1 작습니다.
- 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
- 참가자 중에는 동명이인이 있을 수 있습니다.

##### 입출력 예

| participant                             | completion                       | return |
| --------------------------------------- | -------------------------------- | ------ |
| [leo, kiki, eden]                       | [eden, kiki]                     | leo    |
| [marina, josipa, nikola, vinko, filipa] | [josipa, filipa, marina, nikola] | vinko  |
| [mislav, stanko, mislav, ana]           | [stanko, ana, mislav]            | mislav |

##### 입출력 예 설명

예제 #1
leo는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #2
vinko는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #3
mislav는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.

## 내 코드

```python
def solution(participant, completion):
    map = dict()
    for c in completion:
        map[c] = 0  # 초기화
    for p in participant:
        # 1. 완주자 명단에 없다면 리턴해주자.
        if p not in completion:
            return p
        # 2. 아니면 1 더해주자.
        else:
            map[p]+=1
    for comp in completion:
        if comp not in map:
            return comp
        if map[comp]==1:
          	# 3. 맵에서 지워준다.
            del map[comp]
        else:
          	# 4. 아니면 하나씩 지워준다.
            map[comp]-=1
    return map.popitem()[0]


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant,completion))
```

- 테스트 코드는 다 통과하였지만, 시간 효율 테스트에서는 실패하였음.

## 다른 사람 코드

```python
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]
```

```python
def solution(s,c):
		# 먼저 정렬해준다.
    s.sort()
    c.sort()
		# zip 이라는 함수를 사용해서, 둘을 한바퀴 돌린다.
    for par, com in zip(s, c) :
        if par != com :
            return par   # 예시 1번

    return s[-1]         # 예시 2번

```

```python
# 예시 1번
A = ['a','b','b','c'] 
B = ['a','b','c']
zip(A, B)  # [('a','a'), ('b','b'), ('b','c')]  # 차이 발생

# 예시 2번 - 1
A = ['a','b','c','c']   # 마지막 값 (중복된 값이 맨 뒤에)
B = ['a','b','c']
zip(A, B)  # [('a','a'), ('b','b'), ('c','c')]

# 예시 2번 -2
A = ['a','b','c']       # 마지막 값 (하나 다른 것이 맨 뒤에)
B = ['a','b]
zip(A, B)  # [('a','a'), ('b','b')]
```

```python
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
```

- `Counter()`는 `dict`와 같이 `hash`형 자료들의 값의 개수를 셀 때 사용하는데, 딕셔너리처럼 {'자료 이름' : '개수'} 형식으로 만들어진다!!!!!!!!! 심지어 Counter 객체들끼리 뺄셈도 가능하다 (자세한 건 아래에서)

```python
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
```

- 단순한 덧셈 뺄셈 방식이다. 해시 정수값으로 바꿔준다.

