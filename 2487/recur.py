# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recur(node):
            if node is None:
                return 
            nxt = recur(node.next)
            if nxt and node.val < nxt.val:
                return nxt
            else:
                node.next = nxt
                return node
            
        
        return recur(head)

