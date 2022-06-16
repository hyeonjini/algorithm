import sys
input = sys.stdin.readline

def solution(lottos, win_nums):
   
   rank = [6, 6, 5, 4, 3, 2, 1]
   
   visible = [num for num in lottos if num > 0]
   invisible = [num for num in lottos if num == 0]
   
   min_count = len([v for v in visible if v in win_nums])
   
   return rank[min_count + len(invisible)], rank[min_count]

if __name__ == "__main__":
   lottos = [44, 1, 0, 0, 31, 25]
   win_nums = [31, 10, 45, 1, 6, 19]
   
   # lottos = [0, 0, 0, 0, 0, 0]
   # win_nums = [38, 19, 20, 40, 15, 25]
   print(solution(lottos, win_nums))
