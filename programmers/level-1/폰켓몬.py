def solution(nums):
    can = len(nums) // 2
    nums = set(nums)
    return can if can < len(nums) else len(nums)

if __name__ == "__main__":
    nums = [3, 1, 2, 3]
    nums = [3,3,3,2,2,4]
    print(solution(nums))