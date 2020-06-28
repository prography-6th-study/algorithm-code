def solution(weight):
  # weight를 오름차순으로 정렬합니다.
  weight.sort()
  # answer 1부터 시작합니다. 나중에 1 더하는거 안 까먹을라고
  answer = 1 
  # weight를 순회합니다.
  for w in weight:
    # answer >= w라면, answer에 w를 더해줍니다.
    if answer >= w:
      answer += w
  return answer

"""풀이방법
작은 수부터 순서대로 더 했을 때 누적 값보다 다음 추의 무게가 커지면 그 사이 값은 만들 수 없게 된다
"""