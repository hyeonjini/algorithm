def solution(s):
    def capitalize(s):
        if len(s) <= 1:
            return s.upper()
        return s[0].upper() + s[1:].lower()

    answer = " ".join([capitalize(item) for item in s.split(" ")])
    # print(answer)
    return answer



if __name__ == "__main__":
    assert solution("3people unFollowed me") == "3people Unfollowed Me"
    assert solution("for the last week") == "For The Last Week"
    assert solution("time   to die" ) == "Time   To Die"
    assert solution("the") == "The"
    assert solution("8seconds") == "8seconds"
    assert solution("k") == "K"