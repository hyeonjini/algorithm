def solution(numbers):
    answer = []
    
    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            min_number = number + 1
            while True:
                diff = bin(number ^ min_number)[2:]
                diff = diff.replace("0", "", -1)
                if  len(diff) <= 2:
                    break
                min_number += 1
            answer.append(min_number)

    return answer

if __name__ == "__main__":
    assert solution([2, 7]) == [3, 11]
    assert solution([int(2e8+2e7), int(1e16)])