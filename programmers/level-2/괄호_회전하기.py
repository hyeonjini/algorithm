def solution(s):
    answer = 0

    for i in range(len(s)):
        s = move(s)
        if is_right(s):
            answer += 1

    return answer

def move(s):
    return s[1:] +s[0] 

def is_right(s):
    
    pair = {
        ")":"(",
        "]":"[",
        "}":"{",
    }

    store = []
    for x in list(s):
        if x in ("(", "[", "{"):
            store.append(x)
        else:
            if pair[x] not in store:
                return False
            else:
                if store[-1] != pair[x]:
                    return False
                else:
                    store = store[:-1]
                # x_pair = store.index(pair[x], -1)
                # del store[x_pair]

    return True if len(store) == 0 else False

if __name__ == "__main__":
    assert solution("}]()[{") == 2
    assert solution("[](){}") == 3
    assert solution("[(){}]") == 1
    assert solution("}}}") == 0
    assert solution("(((") == 0
    assert solution("[)(]") == 0
    assert solution("(") == 0
    assert solution(")") == 0
    assert solution("()") == 1
    # assert solution("([{)}]")