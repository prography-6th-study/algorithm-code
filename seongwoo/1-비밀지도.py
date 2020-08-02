"""
3번 테스트케이스 -> 주어지는 값이 0인 경우
출력 예제가 좀 이상하게 나와 있는데, 공백 2개 이상을 1개로 변환하지 않아도 된다.

bin() 함수 쓰면 쉽게 이진수 변환이 가능한데, 자주 안 쓰다보니까 직접 구현하려고 했었다..
벽/공백 부분 확인하는 것도 | 연산으로 더 짧게 구현 가능했을듯.
비트 연산자에 대해서 공부하는 계기가 되었음.
"""

def dec2bin_mine(num, bi, n):
    if num == 0:
        return '00000'
    if num == 1:
        if len(bi) != n:
            bi += (n - len(bi)) * '0'
        return bi
    if num == 2:
        return dec2bin(num // 2, bi + '01', n)
    elif num == 3:
        return dec2bin(num // 2, bi + '11', n)
    elif num % 2 == 0:
        return dec2bin(num // 2, bi + '0', n)
    else:
        return dec2bin(num // 2, bi + '1', n)

def solution(n, arr1, arr2):
    ret = []
    for i in range(n):
        bin1 = bin(arr1[i]).lstrip('0b')
        bin2 = bin(arr2[i]).lstrip('0b')
        if len(bin1) != n:
            bin1 = (n - len(bin1)) * '0' + bin1
        if len(bin2) != n:
            bin2 = (n - len(bin2)) * '0' + bin2
        value = ""
        for x, y in zip(bin1, bin2):
            if x == '1' or y == '1':
                value += '#'
            else:
                value += ' '
        ret.append(value)
    return ret

n = 5
a1 = [9, 20, 28, 18, 11]
a2 = [30, 1, 21, 17, 28]

print(solution(n,a1,a2))
