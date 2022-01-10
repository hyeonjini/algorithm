def solution(relation):
    answer = 0
    col = len(relation[0])
    row = len(relation)
    for i in range(col):
        col_set = set([])
        for r in relation:
            col_set.add(r[i])
        if len(col_set) == row:
            
            answer += 1
        print(col_set)
    
    return answer

if __name__ == "__main__":
    relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    print(solution(relation))