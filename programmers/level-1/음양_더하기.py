def solution(absolutes, signs):
    
    return sum([item for item, sign in zip(absolutes, signs) if sign]) + sum([-item for item, sign in zip(absolutes, signs) if not sign])

if __name__ == "__main__":
    absolutes = [4, 7, 12]
    signs = [True, False, True]
    print(solution(absolutes, signs))