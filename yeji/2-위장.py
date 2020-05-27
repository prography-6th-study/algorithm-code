from collections import defaultdict
def solution(clothes):
  clothesDict = defaultdict(lambda:0)

  for value, key in clothes:
    clothesDict[key] += 1

  result = 1

  for key in clothesDict:
    result *= (clothesDict[key]+1)

  return result-1 #어떤 옷도 착용하지않는 경우 제외