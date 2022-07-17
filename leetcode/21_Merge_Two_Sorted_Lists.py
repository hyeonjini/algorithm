# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass


        
if __name__ == "__main__":
    solution = Solution()
    assert solution.mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4]) == [1,1,2,3,4,4]
    assert solution.mergeTwoLists(list1 = [], list2 = []) == []
    assert solution.mergeTwoLists(list1 = [], list2 = [0]) == [0]