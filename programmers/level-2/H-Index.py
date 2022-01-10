"""
H-Index
"""

def solution(citations):
    answer = 0
    citations.sort()

    n = len(citations)
    for h in range(len(citations) + 1):
        ref = [c for c in citations if c >= h]
        not_ref = [c for c in citations if c <= h]
        print(h, ref, not_ref)
        if len(ref) >= h and len(not_ref) <= h:
            answer = max(answer, h)

    return answer

if __name__ == "__main__":
    # citations = [0]
    # citations = [0, 2, 2]
    citations = [10, 50, 100]
    print(solution(citations))