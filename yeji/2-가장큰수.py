def solution(numbers):
    if set(numbers) == {0}:
        return "0"
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3 , reverse=True)
    answer = ''.join(numbers) 
    return answer

"""풀이방법
1. 0만 있을 때는 바로 0 return
2. numbers 원소를 string으로 형변환
3. numbers 원소가 최고 1000이니까 최소 3자리 수로 만든다
4. 정렬한다(string의 경우 아스키로 변환되서 비교됌)
5. 정렬 결과 붙여줌
"""