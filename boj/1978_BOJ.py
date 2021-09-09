n = int(input())
numbers = list(map(int, input().split()))

result = 0
for number in numbers:
    is_prime = 1
    for i in range(2, number):
        if number % i == 0:
            is_prime = 0
            break
    result += is_prime

print(result)