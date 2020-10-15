def solution(arr):
    def compress(x, y, n):
        check = arr[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != check:
                    compress(x, y, n // 2)
                    compress(x, y + n // 2, n // 2)
                    compress(x + n // 2, y, n // 2)
                    compress(x + n // 2, y + n // 2, n // 2)
                    return
        ret.append(check)
    
    ret = []
    compress(0, 0, len(arr))
    return [ret.count(0), ret.count(1)]