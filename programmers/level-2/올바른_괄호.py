def solution(s):
    stack = []

    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
            continue
        if not stack:
            return False
        stack.pop(-1)

    if not stack:
        return True
    return False

if __name__ == "__main__":
    assert solution("()()") == True
    assert solution("(())()") == True
    assert solution(")()(") == False
    assert solution("(()(") == False


