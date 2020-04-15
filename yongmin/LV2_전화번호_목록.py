def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False

    return True

#test
pb1 = ["119", "97674223", "1195524421"]
pb2 = ["123", "456", "789"]
pb3 = ["12", "123", "1235", "567", "88"]

print(solution(pb1))
print(solution(pb2))
print(solution(pb3))