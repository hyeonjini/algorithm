
def solution(record):
    answer = []
    user_ids = {}
    for data in record:
        data = data.split()
        if data[0] == "Enter":
            user_ids[data[1]] = data[2]
            answer.append([data[1], "님이 들어왔습니다."])

        elif data[0] == "Leave":
            answer.append([data[1], "님이 나갔습니다."])
        
        elif data[0] == "Change":
            user_ids[data[1]] = data[2]

    answer = [user_ids[ans[0]] + ans[1] for ans in answer]
    return answer

if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(record))
