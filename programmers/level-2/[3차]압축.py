def solution(msg):
    answer = []

    word_dict = {}

    for i in range(1, 27):
        word_dict[chr(64 + i)] = i
    
    msg += "@"
    while True:
        w_i = find_current_word(msg, word_dict)
        w = msg[:w_i]
        c = msg[w_i]
        
        if c == "@":
            answer.append(word_dict[w])
            break
        
        if w + c not in word_dict.keys():
            word_dict[w+c] = len(word_dict.keys()) + 1

        answer.append(word_dict[w])
        msg = msg[w_i:]

    return answer

def find_current_word(msg, word_dict):

    word_index = 0
    for i in range(1, len(msg)):
        if msg[:i] in word_dict.keys():
            word_index = i
    return word_index

if __name__ == "__main__":
    assert solution("KAKAO") == [11, 1, 27, 15]
    assert solution("TOBEORNOTTOBEORTOBEORNOT") == [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
    assert solution("ABABABABABABABAB") == [1, 2, 27, 29, 28, 31, 30]
