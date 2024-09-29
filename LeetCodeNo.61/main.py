# 61. Rotate List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Thoughts:
        # 1. put all nodes in a list.
        # 2. rotate the list based on k.
        # 3. reconstruct the linked list based on the current order of the list.

        if head == None or head.next == None:
            return head

        count = 0
        nodes = []

        ptr = head
        while ptr != None:
            nodes.append(ptr)
            ptr = ptr.next
            count += 1
        k = k % count
        while k > 0:
            nodes = [nodes[-1]] + nodes[0:count-1]
            k -= 1
        
        head = nodes[0]
        for idx, value in enumerate(nodes):
            if idx == len(nodes) - 1:
                value.next = None
            else:
                value.next = nodes[idx+1]
        return head



        