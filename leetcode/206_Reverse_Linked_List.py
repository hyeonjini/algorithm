from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        reversed_node = ListNode()
        while head:
            reversed_node.val = head.val
            current_node = ListNode(0, reversed_node)
            reversed_node = current_node
            head = head.next

        return reversed_node.next
