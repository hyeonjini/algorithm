"""
튜플
"""
import sys

def solution(s):
    answer = []
    print(s)
    items = []

    stack = []
    i = 0
    stack.append(s[i])
    group = ''
    while stack:
        i += 1

        if s[i] == "}" and stack[-1] == "{":
            stack.pop()

            if len(group) != 0:
                items.append(group)
                group = ''

        elif s[i] == "{":
            stack.append(s[i])

        else:
            group += s[i]

    # print(items)
    items = [[int(i) for i in item.split(',') if i != ''] for item in items]
    # print(items)
    items.sort(key=lambda x : len(x))

    for group in items:
        for i in range(len(group)):
            if group[i] not in answer:
                answer.append(group[i])

    return answer

input = sys.stdin.readline

if __name__ == "__main__":

    s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
    print(solution(s))