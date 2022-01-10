"""
큰 수 만들기
"""
def solution(number, k):
    stack = []

    for i in range(len(number)):
        # if len(number) - k == len(stack):
        #     break
        if len(stack) == 0 or k <= 0:
            stack.append(number[i])
            continue
        else:
            while True:

                if len(stack) > 0 and int(stack[-1]) < int(number[i]) and k > 0:
                    k -= 1
                    stack.pop()
                else:
                    stack.append(number[i])
                    break
    stack = stack[:len(number)-k]
    # print(stack)/
    return ''.join(stack)

if __name__ == "__main__":
    number = "1924"
    k = 2
    number = "4177252841"
    k = 4
    number = "10"
    k = 1
    print(solution(number, k))