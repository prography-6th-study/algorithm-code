def solution(triangle):
  for r in range(1, len(triangle)):
    for c in range(r+1):
      # 제일 왼쪽일 때
      if c == 0:
        triangle[r][c] += triangle[r-1][c]
      # 제일 오른쪽일 때
      elif r == c:
        triangle[r][c] += triangle[r-1][-1]
      # 나머지
      else:
        triangle[r][c] += max(triangle[r-1][c], triangle[r-1][c-1])
  return max(triangle[-1])

"""풀이방법
밑으로 내려오면서 위의 값이랑 더해나간다
가장 마지막 줄에서 가장 큰 값을 리턴한다
"""