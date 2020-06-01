def solution(operations):
    answer = []
    queue = []
    while len(operations) > 0:
        operation = operations.pop(0)

        if 'I' in operation:
            queue.append(int(operation.split(' ')[1]))
        
        if 'D' in operation:
            if len(queue) == 0:
                continue
            elif '-1' in operation:
                queue.remove(min(queue))
                
            elif '1' in operation:
                queue.remove(max(queue))

    if len(queue) == 0:
        answer = [0, 0]
    else:
        answer = [max(queue), min(queue)]
    return answer