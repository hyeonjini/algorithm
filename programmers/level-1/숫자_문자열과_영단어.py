def solution(s):
    parser = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for word in parser:
        s = s.replace(word, str(parser.index(word)), -1)
    return int(s)


if __name__ == "__main__":
    s = "one4seveneight"
    print(solution(s))