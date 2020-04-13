# level2-전화번호 목록

###### 문제 설명

전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

- 구조대 : 119
- 박준영 : 97 674 223
- 지영석 : 11 9552 4421

전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

##### 제한 사항

- phone_book의 길이는 1 이상 1,000,000 이하입니다.
- 각 전화번호의 길이는 1 이상 20 이하입니다.

##### 입출력 예제

| phone_book                  | return |
| --------------------------- | ------ |
| [119, 97674223, 1195524421] | false  |
| [123,456,789]               | true   |
| [12,123,1235,567,88]        | false  |

##### 입출력 예 설명

입출력 예 #1
앞에서 설명한 예와 같습니다.

입출력 예 #2
한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.

입출력 예 #3
첫 번째 전화번호, “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.

```python
def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        pLen = len(phone_book[i])
        for j in range(i+1,len(phone_book)):
            if phone_book[i] == phone_book[j][:pLen]:
                return False
    return answer
```

- 테스트케이스 2개가 틀렸다고 나옴. 다 도는건데 어디가 잘못된거지?

```python
def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        pLen = len(phone_book[i])
        for j in range(len(phone_book)):
            if phone_book[i] == phone_book[j][:pLen] and i!=j:	# 추가
                return False
    return answer
```

- 사소한 차이었다. 119, 11 의 예시를 생각해내어 알게 되었다. for문을 완전히 두번 돌아야한다.
- 같은 수가 아닌 조건에서 접두어가 같다면 false 를 반환하도록 해야 한다는 것을 알게 되었다.

