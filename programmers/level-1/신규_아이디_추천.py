import re

def solution(new_id):

    print("start :", new_id)
    new_id = upper_to_lower(new_id)
    print(f" 1단계: {new_id}")
    new_id = valid_char(new_id)
    print(" 2단계: ", new_id)
    new_id = merge_dot(new_id)
    print(" 3단계: ", new_id)
    new_id = remove_dot(new_id)
    print(" 4단계: ", new_id)
    new_id = replace_empty_to_a(new_id)
    print(" 5단계: ", new_id)
    new_id = limit_len(new_id)
    print(" 6단계: ", new_id)
    new_id = increase_len(new_id)
    print(" 7단계: ", new_id)
    
    return new_id

# 1단계 대문자 -> 소문자
def upper_to_lower(new_id):
    return new_id.lower()

# 2단계 문자 종류 제한 (alpah, number, -, _, .)
def valid_char(new_id):
    alphabet = [i for i in range(97, 123)]
    numbers = [i for i in range(48, 58)]
    special = [45, 46, 95]
    # new_id = re.sub(r'^[a-z0-9\-_.]', '', new_id)
    temp = ""
    for char in new_id:
        if ord(char) in alphabet:
            temp += char
        if ord(char) in numbers:
            temp += char
        if ord(char) in special:
            temp += char
    
    return temp

# 3단계 연속된 dot 병합
def merge_dot(new_id):
    while ".." in new_id:
        new_id = new_id.replace("..", ".")

    return new_id

# 4단계 처음과 끝 dot 제거
def remove_dot(new_id):

    while len(new_id) > 0 and new_id[0] == ".":
        new_id = new_id[1:]
    
    while len(new_id) > 0 and new_id[-1] == ".":
        new_id = new_id[:-1]
    
    return new_id

# 5단계 빈문자열이면 a대입
def replace_empty_to_a(new_id):
    new_id = "a" if new_id == "" else new_id
    return new_id

# 6단계 16자 이상이면 15자 남기고 제거, 
def limit_len(new_id):

    if len(new_id) > 15:
        new_id = new_id[:15]
    
    new_id = remove_dot(new_id)
    return new_id

# 7단계 2자 이하라면 3이 될 때까지 반복해서 붙이
def increase_len(new_id):
    while len(new_id) < 3:
        new_id = new_id + new_id[-1]

    return new_id

if __name__ == "__main__":
    new_id = "...!@BaT#*..y.abcdefghijklm"
    new_id = "abcdefghijklmn.p"
    new_id = "123_.def"
    new_id = "=.="
    print(solution(new_id))