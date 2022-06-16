def solution(s):
    return ''.join(sorted(list(s), key=lambda x: -ord(x)))


if __name__ == "__main__":
    s = "Zbcdefg"
    print(solution(s))