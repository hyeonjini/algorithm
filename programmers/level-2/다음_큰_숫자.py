def solution(n):
    answer = 0
    target = "{0:b}".format(n).count("1")
    while True:
        n += 1
        if target == "{0:b}".format(n).count("1"):
            answer = n
            break


    return answer



if __name__ == "__main__":

    assert solution(78) == 83
    assert solution(15) == 23