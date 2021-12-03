"""
전화번호 목록
"""

class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.child:
                current_node.child[char] = Node(char)
            current_node = current_node.child[char]
        
        current_node.data = string # 맨 마지막 Node에 data 추가
    
    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.child:
                current_node = current_node.child[char]
            else:
                return False
        
        if current_node.data:
            return True
        else:
            return False
    
    def starts_with(self, prefix):
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.child:
                current_node = current_node.child[p]
            else:
                return None

        current_node = [current_node]
        next_node = []

        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.child.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break
        
        return words
    
    def numbers_starts_with(self, prefix):
        current_node = self.head

        for p in prefix:
            if p in current_node.child:
                current_node = current_node.child[p]
            else:
                return 0

        return len(current_node.child)

    
def solution(n, phone):

    trie = Trie()
    # 전화번호 Trie 자료구조에 insert
    for phone in phones:
        trie.insert(phone)
    
    # 하나의 번호가 다른 번호의 prefix인지 검사
    for phone in phones:
        if trie.numbers_starts_with(phone) > 0:
            return False
    
    return True

if __name__ == "__main__":

    tc = int(input())
    answers = []
    for _ in range(tc):
        n = int(input())
        phones = []
        for _ in range(n):
            phones.append(input().rstrip())
        
        if solution(n, phones):
            answers.append("YES")
        else:
            answers.append("NO")
    
    for answer in answers:
        print(answer)



