# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        currentNode = head

        while currentNode != None:

            while len(stack) > 0 and stack[-1].val < currentNode.val:
                stack.pop()

            stack.append(currentNode)
            currentNode = currentNode.next

        currentNode = stack.pop()
        currentNode.next = None

        while len(stack) > 0:
            head = stack.pop()
            head.next = currentNode
            currentNode = head
        
        return currentNode



