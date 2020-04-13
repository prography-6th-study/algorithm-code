def solution(phone_book):
    phone_book.sort(key=len)

    for i in range(len(phone_book)):
        lenOfi = len(phone_book[i])
        curphone = phone_book[i]
        for j in range(i+1,len(phone_book)):
            if curphone == phone_book[j][:lenOfi]:
                return False
    return True
