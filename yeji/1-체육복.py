def solution(n, lost, reserve):
    _reserve = [ r for r in reserve if r not in lost ]
    _lost = [ l for l in lost if l not in reserve ]
    
    for r in _reserve:
        front = r - 1
        back = r + 1
        
        if f in _lost:
            _lost.remove(front)
        
        elif b in _lost:
            _lost.remove(back)
    
    return n - len(_lost)