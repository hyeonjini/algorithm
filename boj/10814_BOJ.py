import sys
input = sys.stdin.readline

n = int(input())

person = []

for i in range(n):
    age, name = input().split()
    person.append([i, int(age), name])

person.sort(key=lambda x: (x[1], x[0]))

for p in person:
    print(p[1], p[2])