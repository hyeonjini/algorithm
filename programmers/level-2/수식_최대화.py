from itertools import permutations
import copy

def solution(expression):
    answer = 0

    expression_to_list = []
    digit = ""
    for i in range(len(expression)):
        if expression[i].isdigit():
            digit += expression[i]
        else:
            expression_to_list.append(digit)
            digit = ""
            expression_to_list.append(expression[i])
    expression_to_list.append(digit)

    operator = set([e for e in expression if e in ("+", "-", "*")])
    cases = list(permutations(operator, len(operator)))

    for case in cases:
        answer_of_case = calculate_with_rank(copy.deepcopy(expression_to_list), case)
        # answer_of_case = calculate_with_rank(copy.deepcopy(expression_to_list), ["*", "+", "-"])
        answer = max(answer, answer_of_case)
    return answer

def calculate_with_rank(expression, case):
    
    for c in case:
        stack = []
        while len(expression) > 0:
            e = expression.pop(0)
            if e == c:
                stack.append(str(calculate(int(stack.pop()), int(expression.pop(0)), e)))
            else:
                stack.append(e)

        expression = stack

    return abs(int(expression[0]))

def calculate(a, b, op):
    cal = {
        "-": a - b,
        "*": a * b,
        "+": a + b,
    }
    return cal[op]

if __name__ == "__main__":
    assert solution("100-200*300-500+20") == 60420
    assert solution("50*6-3*2") == 300
    assert solution("100+500-2*1")
    assert solution("500*0-100")
    assert solution("500*1-100")

    assert solution("500-200-300-100+1+1*0*0")
    print(solution("1*2-3+4*2"))