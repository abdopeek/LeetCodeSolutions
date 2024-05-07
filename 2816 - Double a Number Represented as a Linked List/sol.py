# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = 0
        while head:
            stack.append(head.val)
            head = head.next
        
        tail = None
        while stack or cur != 0:
            new_tail = ListNode(0, tail)
            if stack:
                cur += stack.pop() * 2
            new_tail.val = cur % 10
            cur //= 10
            tail = new_tail
        return tail
