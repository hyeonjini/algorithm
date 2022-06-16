import sys
input = sys.stdin.readline

def solution(id_list, report, k):
    reported = {}
    for id in id_list:
        reported[id] = 0

    report_to_dict = {}
    for id in id_list:
        report_to_dict[id] = set()
    

    for r in report:
        user, target = r.split()
        report_to_dict[user].add(target)

    for user in id_list:
        for target in report_to_dict[user]:
            reported[target] += 1


    banned = [user for user, count in reported.items() if count >= k]

    answer = []
    for user in id_list:
        mailed = 0
        for target in report_to_dict[user]:
            if target in banned:
                mailed += 1
        answer.append(mailed)
    return answer


if __name__ == "__main__":
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2
    print(solution(id_list, report, k))