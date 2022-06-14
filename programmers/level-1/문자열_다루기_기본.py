def solution(s):
    return (4 == len(s) or len(s) ==6) and s.isdigit()

if __name__ == "__main__":
    print(solution("a234"), solution("1234"))