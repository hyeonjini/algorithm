"""
구명보트
"""
def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    right = len(people) - 1

    while left <= right:
        total = people[left] + people[right]

        if total <= limit:
            left += 1
            right -= 1
            answer += 1
        
        elif total > limit:
            right -= 1
            answer += 1

    return answer

if __name__ == "__main__":
    people = [70, 50, 50, 80]
    limit = 100
    print(solution(people, limit))
    