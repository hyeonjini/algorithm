"""연산자 끼워 넣기"""

import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div

    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0 :
            add -= 1
            dfs(i + 1, now + number[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - number[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * number[i])
            mul += 1

        if div > 0:
            div -= 1
            dfs(i + 1, int(now / number[i]))
            div += 1

dfs(1, number[0])


print(min_value)
print(max_value)