def solution(n, arr1, arr2):
    # answer = [[""] * n for _ in range(n)]
    
    # for i, (x1, x2) in enumerate(zip(arr1, arr2)):
    #     x1 = format(x1, f"0{n}b")
    #     x2 = format(x2, f"0{n}b")

    #     for j in range(n-1, -1, -1):
    #         answer[i][j] = "#" if x1[j] == "1" or x2[j] == "1" else " "

    # return ["".join(line) for line in answer]
    answer = []
    for x1, x2 in zip(arr1, arr2):
        x = str(bin(x1|x2)[2:])
        x = x.rjust(n, '0')
        x = x.replace("1", "#")
        x = x.replace("0", " ")

        answer.append(x)

    return answer
if __name__ == "__main__":
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    print(solution(n, arr1, arr2))