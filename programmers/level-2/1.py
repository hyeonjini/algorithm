"""
sol) 
2 pointer로 해결
사람의 몸무게와 보트의 몸무게 입력값을 고려했을때 무조건 2명만 태울 수 있음
양쪽 끝에서 탐색하면서 무거운 사람과 가벼운사람의 합이 limit을 넘기면 가벼운 사람을 지정하는 i를 키움

"""
def solution(people, limit):
    answer = 0
    people.sort()
    i = 0
    j = len(people) - 1
    
    while i <= j:
        answer += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return answer

if __name__ == "__main__":
    people = [50, 50, 50, 50, 70, 80]
    limit = 100

    print(solution(people, limit))