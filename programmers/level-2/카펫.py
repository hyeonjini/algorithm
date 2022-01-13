"""
카펫
"""
def solution(brown, yellow):
    answer = -1

    max_width = (brown - 2) // 2
    for w in range(max_width, 2, -1):
        for h in range(3, w + 1):
            rectangle = w * h
            if (rectangle - brown) == yellow:
                return w, h

    return answer

if __name__ == "__main__":
    brown = 24
    yellow = 24

    print(solution(brown, yellow))