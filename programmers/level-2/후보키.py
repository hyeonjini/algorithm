from itertools import combinations
import copy
def solution(relation):
    answer = 0
    col = [i for i in range(len(relation[0]))]
    
    candidate_key = []
    keys = []
    for i in range(1, len(col) + 1):
        keys += list(combinations(col, i))


    for key in keys:
        candidate = set([])
        for row in relation:
            select = []
            for i in key:
                select.append(row[i])

            candidate.add("".join(select))
        
        if len(candidate) == len(relation):
            if not candidate_key:
                candidate_key.append(key)
                continue

            if not any([set(ck).issubset(key) for ck in candidate_key]):
                candidate_key.append(key)
    # print(candidate_key)

    return len(candidate_key)

if __name__ == "__main__":
    relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    print(solution(relation))