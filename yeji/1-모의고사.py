from itertools import cycle

def solution(answers):
    student_1 = [1,2,3,4,5]
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = {1: 0 , 2: 0 , 3: 0}
    winner = []

    for s1, s2, s3, answer in zip(cycle(student_1), cycle(student_2), cycle(student_3), answers):
        if s1 == answer:
            scores[1] += 1
        if s2 == answer:
            scores[2] += 1
        if s3 == answer:
            scores[3] += 1

    for name, score in scores.items():
        if score == max(scores.values()):
            winner.append(name)
    return winner
    
    """풀이방법
    cycle을 이용하여 answers에 맞게 배열을 만들어줌
    
    처음엔 return [max(scores.items(), key=scores.get)] 이렇게 했는데 
    그러면 동점자가 있어도 한명만 나와서 위의 방식으로 처리함

    지금 생각해보면 scores 굳이 dictionary 사용 안해도 될꺼 같다
    """