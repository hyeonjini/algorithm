"""
순위 검색
"""
def binary_search(arr, target, key):
    
    left = 0
    right = len(arr) - 1

    mid = (left + right) // 2
    # print("target:", target)
    while left <= right:

        # print(left, right)
        mid = (left + right) // 2

        if target < int(arr[mid][key]):
            right = mid - 1

        elif target > int(arr[mid][key]):
            left = mid + 1
        
        else: # target 과 mid가 같은 경우 mid를 1씩 줄여보면서 변화는 부분 찾기
            while mid > 0:
                mid -= 1
                if target > int(arr[mid][key]):
                    return mid + 1
            return mid
    # print("arr[mid]:", arr[mid][key], "target:", target)
    return mid + 1 if int(arr[mid][key]) < target else mid

def solution(info, query):
    answer = []

    info = [item.split() for item in info]
    info.sort(key=lambda x : int(x[-1])) # score 내림차순 정렬
    query = [[sub for sub in item.split() if sub != "and"] for item in query]

    # for i in info:
    #     print("info", i)
    # print('query', query)
    
    for q in query:
        count = 0
        # print(q)
        start = binary_search(info, int(q[-1]), 4)


        for i in range(len(info[start:])):

            app = info[start + i]
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