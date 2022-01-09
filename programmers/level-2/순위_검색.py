"""
순위 검색
"""
def solution(info, query):
    answer = []

    info = [item.split() for item in info]
    info.sort(key=lambda x : -int(x[-1])) # score 내림차순 정렬
    query = [[sub for sub in item.split() if sub != "and"] for item in query]

    for q in query:
        count = 0
        for i in range(len(info)):
            app = info[i]
            if int(app[-1]) < int(q[-1]):
                break
            if not (q[0] == app[0] or q[0] == "-"):
                continue
            if not (q[1] == app[1] or q[1] == "-"):
                continue
            if not (q[2] == app[2] or q[2] == "-"):
                continue
            if not (q[3] == app[3] or q[3] == "-"):
                continue
            
            count += 1
            
        answer.append(count)

    return answer

if __name__ == "__main__":
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    print(solution(info, query))