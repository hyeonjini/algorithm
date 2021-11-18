"""
1부터 n까지 번호가 붙어있는 n명의 사람이 영어 끝말잇기 하고 있다.
1. 1번부터 번호 순서대로 한 사람씩 차례대로 단어를 말함
2. 마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작
3. 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야함
4. 이전에 등장했던 단어는 사용할 수 없음
5. 한글자인 단어는 인정되지 않음

ex) tank -> kick -> know -> wheel -> land -> dream -> mother -> robot -> tank
3번 사람 탈락

sol) 
앞에서 말한 단어와 현재 단어가 이어지지 않으면 탈락
이미 제시한 단어를 또 제시하면 탈락
구현 문제로 해결
"""

def solution(n, words):
    answer = []
    history = [words[0]]
    for i in range(1, len(words)):
        if words[i] not in history:
            if history[i-1][-1] != words[i][0]:
                print(i)
                print((i // n) + 1, i % n + 1)
                answer.append(i % n + 1)
                answer.append(i // n + 1)
                return answer
            history.append(words[i])
        else:
            answer.append(i % n + 1)
            answer.append(i // n + 1)
            return answer
    answer = [0, 0]
    return answer

if __name__ == "__main__":
    n = 3
    words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
    print(solution(n, words))