# Definition for singly-linked list.

from typing import Optional
from heapq import heappush, heappop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        q = []
        
        while list1:
            heappush(q, list1.pop(-1))
        
        while list2:
            heappush(q, list2.pop(-1))


        answer = []
        while q:
            answer.append(heappop(q))

        return answer



        
if __name__ == "__main__":
    solution = Solution()


    assert solution.mergeTwoLists(list1 = [ListNode(1, 2), ListNode(2, 4), ListNode(4)], list2 = [ListNode(1, 3), ListNode(3, 4), ListNode(4)]) == [ListNode(1,1), ListNode(1,2), ListNode(2,3), ListNode(3, 4), ListNode(4,4), ListNode(4)]
    assert solution.mergeTwoLists(list1 = [], list2 = []) == []
    assert solution.mergeTwoLists(list1 = [], list2 = [ListNode(0)]) == [ListNode(0)]