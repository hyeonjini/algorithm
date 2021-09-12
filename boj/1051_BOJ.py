import sys

input = sys.stdin.readline

n, m = map(int, input().split())

rectangle = []

for _ in range(n):
    rectangle.append(list(input()[:-1]))

max_value = min(n,m)

result = 0

for i in range(n):
    for j in range(m):
        for k in range(max_value):
            if i+k < n and j+k < m:
                if rectangle[i][j] == rectangle[i][j+k] and rectangle[i][j] == rectangle[i+k][j] and rectangle[i][j] == rectangle[i+k][j+k]:
                    result = max(result, (k+1)**2)
print(result)