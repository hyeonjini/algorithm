"""
n행 m열의 격자가 있다. 격자의 행은 0, 1, ... n-1 열은 0, 1, m-1 번의 번호가 순서대로 매겨져 있다.
이 격자에 공을 하나 두고, 그 공에 다음과 같은 쿼리를 날리고자 한다.
- 열번호가 감소하는 방향으로 dx 칸 이동하는 쿼리(query(0, dx))
- 열 번호가 증가하는 방향으로 dx 칸 이동하는 쿼리 (query(1, dx))
- 행 번호가 감소하는 방향으로 dx 칸 이동하는 쿼리(qeury(2, dx))
- 행번호가 증가하는 방향으로 dx 칸 이동하는 쿼리(qeury(3, dx))

단, 공은 격자 바깥으로 이동할 수 없으며, 목적지가 격자 바깥인 경우 공은 이동하다가 더 이상 이동할 수 없을때 멈추게 된다.
ex) 5행 x 4열 크기의 격자 내의 공이 3, 2에 있을때 (3,10) 쿼리를 받는 경우 공은 4행 2열에서 멈추게 된다..
"""

def solution(n, m, x, y, queries):
    answer = -1
    point = [y, y + 1, x, x + 1]
    dir = [-1, 1, -1, 1]
    boundary =  [0, m, 0, n]
    limit = [m, m, n, n]

    for query in queries[:: -1]:
        command = query[0]
        dx = query[1]

        reverse = command ^ 1
        # print(command, reverse)
        point[reverse] += dir[reverse] * dx
        point[reverse] = max(min(point[reverse], limit[reverse]), 0)

        if point[command] != boundary[command]:
            point[command] += dir[reverse] * dx
            point[command] = max(min(point[command], limit[command]), 0)
        
        if point[0] == m or point[1] == 0 or point[2] == n or point[3] == 0:
            return 0

    answer = (point[1] - point[0]) * (point[3] - point[2])
    return answer

if __name__ == "__main__":
    n = 2
    m = 5
    x = 0
    y = 1
    queries = [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]
    print(solution(n, m, x, y, queries))
