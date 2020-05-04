def solution(N):
    x = fibonacci(N+1)
    y = fibonacci(N)

    answer = (x+y) * 2
    return answer

def fibonacci(num): 
    a, b = 0, 1 
    
    for i in range(num): 
        a, b = b, a+b 
    
    return a

"""풀이방법
타일 한변의 길이가 피보나치로 늘어남
둘레니까 x+y하고 곱하기 2
"""