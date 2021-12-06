def solution(n, lost, reserve):
    answer = 0
    student = [1] * (n + 1)
    
    for l in lost:
        student[l] -= 1
    
    for r in reserve:
        student[r] += 1
    
    for i in range(1, n):
        if student[i] == 0:
            if student[i-1] == 2:
                student[i-1] -= 1
                student[i] = 1
                continue
                
            elif student[i+1] == 2:
                student[i+1] -= 1
                student[i] = 1
                continue
    student = [1 for s in student if s > 0]
    answer = sum(student) -1
    return answer

if __name__ == "__main__":
    n = 3
    lost = [3]
    reserve = [1]
    print(solution(n, lost, reserve))