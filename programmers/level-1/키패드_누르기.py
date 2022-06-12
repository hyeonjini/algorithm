def solution(numbers, hand):
    answer = ""
    number_pos = [
        [3, 1], 
        [0, 0], [0, 1], [0, 2], 
        [1, 0], [1, 1], [1, 2],
        [2, 0], [2, 1], [2, 2]
    ]
    l_pos = [3, 0]
    r_pos = [3, 2]

    for number in numbers:
        if number in [1, 4, 7]:
            l_pos = number_pos[number]
            answer += "L"
            continue
        if number in [3, 6, 9]:
            r_pos = number_pos[number]
            answer += "R"
            continue
        
        l_dist = get_distance(l_pos, number_pos[number])
        r_dist = get_distance(r_pos, number_pos[number])
        if l_dist == r_dist:

            if hand == "right":
                r_pos = number_pos[number]
                answer += "R"

            else:
                l_pos = number_pos[number]
                answer += "L"
            
            continue
        
        if l_dist < r_dist:
            l_pos = number_pos[number]
            answer += "L"
        else:
            r_pos = number_pos[number]
            answer += "R"
        
    return answer

def get_distance(current_pos, target):
    return abs(current_pos[0] - target[0]) + abs(current_pos[1] - target[1])

if __name__ == "__main__":
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
    hand = "right"

    print(solution(numbers, hand))