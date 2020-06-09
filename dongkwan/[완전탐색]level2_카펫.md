###### 문제 설명

Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

![carpet.png](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/b1ebb809-f333-4df2-bc81-02682900dc2d/carpet.png)

Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

##### 제한사항

- 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
- 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
- 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

##### 입출력 예

| brown | yellow | return |
| ----- | ------ | ------ |
| 10    | 2      | [4, 3] |
| 8     | 1      | [3, 3] |
| 24    | 24     | [8, 6] |

[출처](http://hsin.hr/coci/archive/2010_2011/contest4_tasks.pdf)

※ 공지 - 2020년 2월 3일 테스트케이스가 추가되었습니다.
※ 공지 - 2020년 5월 11일 웹접근성을 고려하여 빨간색을 노란색으로 수정하였습니다.

- 풀이

```python
def solution(brown, yellow):
    li = []
    for i in range(1,yellow+1):
        if yellow % i == 0:
            li.append(i)
    if len(li) % 2 == 0:
        p1 = li[len(li) // 2 - 1] + 2
        p2 = li[len(li) // 2] + 2
        answer = [p2,p1]
    else:
        if len(li) == 1:
            p1 = li[0] + 2
        else:
            p1 = li[len(li) // 2 + 1] + 2
        answer = [p1,p1]

    return answer
```

- 노랑을 기준으로 약수를 구해서 중앙값 + 2 를 해주면 최소가 될 것이라 가정하고 풀었다.
- 틀림

```python
def solution(brown, yellow):
    li = []
    # 약수 알고리즘 이용! 나머지가 0인거 추가해주기
    for i in range(1,yellow+1):
        if yellow % i == 0:
            li.append(i)
    for i in li:
        j = yellow // i
        # 전체 사각형의 갯수에서 노랑이 빼준게 갈색이라면 그게 정답!
        if ((i+2) * (j+2)) - yellow == brown:
            answer = [i+2,j+2]
    # 가로 세로 길이의 조건에 맞게 내림차순 정렬해준다.
    answer.sort(reverse=True)

    return answer
```

- 조건을 하나 더 추가해주었다.
- 전체 사각형의 갯수에서 노랑색의 개수를 뺴준 것이 갈색이면 그게 가로세로의 길이이다.
- 여기서 `i, j`는 가로 or 세로의 후보이다. 뭐가되었던 정렬해주면 되니까 관계없음!