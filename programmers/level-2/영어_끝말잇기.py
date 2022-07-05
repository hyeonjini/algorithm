def solution(n, words):
    answer = [0, 0]

    appear = set([]) 

    pre_word = words[0][0]
    for i, word in enumerate(words):
        if not word.startswith(pre_word[-1]) or word in appear:
            answer = [i%n + 1, i // n + 1]
            break
        pre_word = word
        appear.add(word)
        

    return answer


if __name__ == "__main__":
    assert solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]) == [3, 3]
    assert solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]) == [0, 0]
    assert solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]) == [1, 3]