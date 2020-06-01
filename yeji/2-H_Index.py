def solution(citations):
    for i,x in enumerate(sorted(citations)):
        if x >= len(citations)-i:
            return len(citations)-i
    return 0