from collections import Counter

def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()  # 문자열을 전부 소문자로
    A, B = [], []  # 다중 집합을 만들 변수

    # 다중집합 A, B 구하기
    for i in range(len(str1) - 1):
        # 두 원소가 문자이면
        if str1[i].isalpha() and str1[i+1].isalpha():
            A.append(str1[i:i+2])  # A에 슬라이싱한 2자리 문자열 추가
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            B.append(str2[i:i+2])

    # 집합 A, B가 공집합인 경우
    if len(A) == 0 and len(B) == 0:
        return 65536

    A, B = Counter(A), Counter(B)  # A, B를 카운터 객체로 변환
    union, intersection = A | B, A & B  # 합집합, 교집합 구하기
    rate = sum(intersection.values()) / sum(union.values())  # 유사도 구하기
    return int(rate * 65536)


# test
print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))