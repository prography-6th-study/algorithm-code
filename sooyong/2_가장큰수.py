# previous code 

from itertools import permutations
numbers = [3, 30, 34, 5, 9]
total = list(permutations(numbers))
maxNum = 0
curNum = 0
for i in range(len(total)):
  for j in range(len(total[i])):
    curNum += str(total[i][j])
  curNum = int(curNum)
  maxNum = max(curNum, maxNum)
  curNum = 0
print(maxNum)

# what I learned from others code

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
