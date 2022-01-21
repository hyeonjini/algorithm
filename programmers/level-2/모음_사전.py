"""
모음 사전
"""

word_idx = {
    
    "A":0,
    "E":1,
    "I":2,
    "O":3,
    "U":4
}
word_value = ["A", "E", "I", "O", "U"]

def solution(word):
    answer = 0

    stack = []
    while True:
        
        answer += 1
        if len(stack) <= 4:
            stack.append("A")
        
        else:
            while True:
                last = stack.pop()
                if last == "U":
                    continue
                else:
                    next_word = word_value[(word_idx[last] + 1) % 5]
                    stack.append(next_word)
                    break
        
        # print(stack)
        if "".join(stack) == word:
            break

    return answer


if __name__ == "__main__":
    word = "EIO"
    print(solution(word))