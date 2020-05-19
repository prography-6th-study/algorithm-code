def solution(numbers, target):
    answer = 0
    len_numbers = len(numbers)

    def operator(index=0):
        if index < len_numbers:
            numbers[index] *= 1
            operator(index+1)

            numbers[index]*=(-1)
            operator(index+1)
        
        elif sum(numbers) == target:
            nonlocal answer
            answer += 1
    
    operator()
    return answer

"""
풀이방법
처음엔 조건을 잘못읽어서 numbers에 들어가 있는 숫자가 1만 있는줄알고 
+,- 조합의 모든 경우의 수를 구했다.
문제를 잘 읽어야한다..
어휴 난 dfs 진짜 모르겠다
"""