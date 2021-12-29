"""
짝지어 제거하기
"""

def solution(s):
    stack = []

    for i in range(len(s)):

        if len(stack) == 0: # 아무것도 없으면 stack에 push
            stack.append(s[i])
            continue

        if stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    return 1 if len(stack) == 0 else 0

if __name__ == "__main__":
    s = "cdcd"
    print(solution(s))