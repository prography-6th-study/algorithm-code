def solution(files):
    num_idx = 0
    splited_files, ret = [], []
    for file in files:
        for ele in file: # file이 img12.png라면
            if ele.isdigit():
                num_idx = file.index(ele)
                break
        head = file[:num_idx] # head = "img"
        next_head = file[num_idx:]
        tail_idx = len(file)  # tail이 없는 경우를 위함
        cnt = 0 
        for ele in next_head:
            cnt += 1
            if cnt == 5: # NUMBER은 최대 길이가 5라는 조건이 있음
                tail_idx = num_idx + 5 
            if ele.isalpha():
                tail_idx = next_head.index(ele) + num_idx - 1
                break
        print(tail_idx)
        number = file[num_idx:tail_idx] # number = "12"
        tail = file[tail_idx:] # tail = ".png"
        splited_files.append([head, head.lower(), number, tail, files.index(file)])
    print(splited_files)
    splited_files.sort(key=lambda x: (x[1], int(x[2]), x[4])) 
    for each_file in splited_files:
        ret.append(each_file[0] + each_file[2] + each_file[3])
    return ret

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
print(solution(["img000012345", "img1.png","img2","IMG02"]))