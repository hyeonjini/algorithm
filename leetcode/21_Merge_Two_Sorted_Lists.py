# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(-1)
        current_node = head

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                current_node.next = list1
                list1 = list1.next

            else:
                current_node.next = list2
                list2 = list2.next

            current_node = current_node.next

        if list1 != None:
            current_node.next = list1
        else:
            current_node.next = list2

        return head.next



        
if __name__ == "__main__":
    solution = Solution()