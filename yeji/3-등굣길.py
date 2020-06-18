def solution(m, n, puddles):
    # 배열 index이용해서 계산하기 편하게 m+1, n+1해서 0으로 덮어줍니다
    answer = [ [0]*(m+1) for i in range(n+1)]
    # 집
    answer[1][1] = 1

    for i in range(1,n+1):
      for j in range(1, m+1):
        # 시작점일 때
        if i==1 and j==1:
          continue
        #연못은 지나갈 방법이 없으니까 0으로
        if [j,i] in puddles:
          answer[i][j] == 0
        else:
          answer[i][j] = answer[i][j-1] + answer[i-1][j]
    return answer[n][m]%1000000007


"""풀이방법
초딩땐가..중딩땐가...최단거리로 가는 방법 몇개인지 찾는 수학문제 다들 기억나유..?
그때 풀던 방식으로 풀었는데 뭐라고 설명해야할지 모르게따..
"""