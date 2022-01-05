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

# def solution(phone_book):
#     for i in range(len(phone_book)): 
#         pivot = phone_book[i] 
#         for j in range(i+1, len(phone_book)): 
#             strlen = min(len(pivot), len(phone_book[j])) 
#             if pivot[:strlen] == phone_book[j][:strlen]: 
#                 return False 
            
#     return True

def solution(phone_book):
    answer = True
    phone_book_dict = {}

    for phone in phone_book: # O(N)
        phone_book_dict[phone] = True
    
    for phone in phone_book: # O(N)
        for i in range(1, len(phone)): # O(1)
            if phone[:i] in phone_book_dict:
                answer = False
    
    return answer

if __name__ == "__main__":

    phone_book = ["119", "97674223", "1195524421"]
    print(solution(phone_book))