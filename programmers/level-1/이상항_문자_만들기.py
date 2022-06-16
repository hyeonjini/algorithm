def solution(s):

    # original = []
    # converted = []

    # for k in s.split():
    #     original.append(k)
    #     converted.append("".join([j.upper() if i % 2 == 0 else j.lower() for i, j in enumerate(k)]))

    # for o, c in zip(original, converted):
    #     s = s.replace(o, c, 1)
    answer = []
    s = s.split(" ")

    for word in s:
        token = []
        for i in range(len(word)):
            token.append(word[i].upper() if i % 2 == 0 else word[i].lower())
        
        answer.append("".join(token))
    
    return " ".join(answer)

s = "try try    tryyy try"
print(solution(s))