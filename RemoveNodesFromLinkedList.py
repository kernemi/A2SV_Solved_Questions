# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        stack = []

        while current:
            while stack and stack[-1] < current.val:
                stack.pop()
            stack.append(current.val)
            current = current.next
        
        temp = ListNode(0)
        current = temp

        for x in stack:
            current.next = ListNode(x)
            current = current.next
        
        return temp.next

        
        


        
