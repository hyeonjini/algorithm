"""
H-Index는 과학자의 생산성과 영향력을 나타내는 지표
어느 과학자의 H-Index를 나타내는 값인 h를 구하고자함

H-Index:
발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면
h의 최댓값이 과학자의 H-Index

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때 H-Index를 구하라

ex) 3, 0, 6, 1, 5 => 3
발표한 논문의 수는 5편, 그중 3편이 3회 이상 인용되었고 나머지 2편의 논문은 3회 이하로 인용

sol)
내림차순으로 정렬하면 (6, 5, 3, 1, 0)

"""
def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort(reverse=True)
    print(citations)
    i = 1
    for j in range(0, len(citations)):
        if citations[j] == i:
            answer = i
            break
        if citations[j] < i:
            answer = i - 1
            break
        i += 1
    return answer
if __name__ =="__main__":
    citations =	[4, 4, 4, 5, 0, 1, 2, 3]
    print(solution(citations))