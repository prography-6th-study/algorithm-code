def solution(files):
    array = []
    for file in files:
        info = [file]  # info에 파일명 전체를 넣는다
        file = file.lower()  # 소문자로 변환

        number_idx, tail_idx = -1, -1  # 숫자 시작 인덱스, 꼬리 시작 인덱스
        for i in range(len(file)):
            # 현재 글자가 숫자형 and 아직 숫자형이 나온적 없으면 number 부분 시작
            if file[i].isnumeric() and number_idx == -1:
                number_idx = i
            # number 부분이 진행중 and 현재 글자가 숫자형이 아니면 tail 부분 시작
            if number_idx != -1 and not file[i].isnumeric():
                tail_idx = i
                break

        info.append(file[:number_idx])  # head
        # tail이 없음 or 숫자가 5자리를 넘어가면 number_idx 부터 최대 5자리까지가 number
        if tail_idx == -1 or tail_idx - number_idx > 5:
            info.append(int(file[number_idx:number_idx + 5]))
        # 아니면 number_idx 부터 tail_idx 사이가 number
        else:
            info.append(int(file[number_idx:tail_idx]))
        array.append(info)

    array.sort(key=lambda x: (x[1], x[2]))  # head, number 기준으로 정렬
    return [x[0] for x in array]


# test
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
print(solution(["img000012345", "img1.png,img2", "IMG02"]))
