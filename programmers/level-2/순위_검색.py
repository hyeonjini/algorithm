"""
순위 검색
"""
from collections import defaultdict
from itertools import combinations
lang = {
    "cpp":0,
    "java":1,
    "python":2
}
position = {
    "backend":0,
    "frontend":1,
}
career = {
    "junior":0,
    "senior":1
}
food = {
    "chicken":0,
    "pizza":1
}

def binary_search(arr:list, target:int):
    
    left = 0
    right = len(arr) - 1

    mid = (left + right) // 2
    if mid == -1 :
        return 0
    while left <= right:

        mid = (left + right) // 2

        if target < int(arr[mid]):
            right = mid - 1

        elif target > int(arr[mid]):
            left = mid + 1
        
        else: # target 과 mid가 같은 경우 mid를 1씩 줄여보면서 변화는 부분 찾기
            # while mid > 0:
            #     mid -= 1
            #     if target > int(arr[mid][key]):
            #         return mid + 1
            # return mid
            right = mid - 1
    
    return mid + 1 if int(arr[mid]) < target else mid

def solution(infos, query):
    answer = []

    infos = [item.split() for item in infos]
    query = [[sub for sub in item.split() if sub != "and"] for item in query]

    applicants = defaultdict(list)

    for info in infos:
        
        attr = info[:4]
        score = int(info[-1])

        idx = [0, 1, 2, 3]
        for i in range(5):
            idx_comb = list(combinations(idx, i))
            
            for j in idx_comb:
                temp = attr.copy()
                for k in j:
                    temp[k] = "-"
                # print("".join(temp))
                applicants["".join(temp)].append(score)
    
    for values in applicants.values():
        values.sort()

    # print(applicants)

    for q in query:
        key = "".join(q[:4])
        score = int(q[-1])

        scope = applicants[key]
        start = binary_search(scope, score)

        answer.append(len(scope) - start)

    return answer

if __name__ == "__main__":
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    print(solution(info, query))