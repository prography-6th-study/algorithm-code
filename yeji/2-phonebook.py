def solution(phone_book):
    phone_book.sort()
    for phone1, phone2 in zip(phone_book, phone_book[1:]):
        if phone1 in phone2:
            return False
    return True