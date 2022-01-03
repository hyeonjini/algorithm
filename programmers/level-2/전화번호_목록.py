"""
전화번호 목록
"""
import sys
input = sys.stdin.readline

# def solution(phone_book):

#     phone_book.sort()

#     for p1, p2 in zip(phone_book, phone_book[1:]):
#         if p2.startswith(p1):
#             return False

#     return True

def solution(phone_book):
    for i in range(len(phone_book)): 
        pivot = phone_book[i] 
        for j in range(i+1, len(phone_book)): 
            strlen = min(len(pivot), len(phone_book[j])) 
            if pivot[:strlen] == phone_book[j][:strlen]: 
                return False 
            
    return True

if __name__ == "__main__":

    phone_book = ["123","456","789"]
    print(solution(phone_book))