"""
먼저 배포되어야 하는 것이 배포 가능할 때, 
while문을 돌면서 같이 배포 가능한 것을 list로부터 같이 pop시키고, 같이 pop된 개수를 result에 넣어 반환.
"""

def solution(progresses, speeds):
    deploy, ret = [], []
    deploy.extend(reversed(progresses))
    speeds.reverse()
    while deploy:
        idx = 0
        cnt = 0
        for i, j in zip(deploy, speeds):
            deploy[idx] = i + j
            idx += 1
        if deploy[-1] >= 100:
            while deploy[-1] >= 100:
                cnt += 1
                deploy.pop(-1)
                speeds.pop(-1)
                if not deploy:
                    break
            ret.append(cnt)
    return ret

p = [93, 30, 55]
s = [1, 30, 5]

print(solution(p,s))