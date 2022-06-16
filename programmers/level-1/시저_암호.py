def solution(s, n):

    answer = ""
    for i in range(len(list(s))):
        if s[i].isalpha():
            asc = ord(s[i])
            if s[i].isupper():
                answer += chr(asc + n) if asc + n < 91 else chr(asc + n - 26)
            else:
                answer += chr(asc + n) if asc + n < 123 else chr(asc + n - 26)
        else:
            answer += s[i]

    return answer

s = "a B z"	
n = 4
print(solution(s, n))