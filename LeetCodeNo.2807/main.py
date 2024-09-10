# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _find_common_divisor(self, val1, val2):
        min_val = min(val1, val2)
        for try_val in range(min_val, 0, -1):
            if val1 % try_val == 0 and val2 % try_val == 0:
                return try_val
        return 1

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        all_nodes = []
        while ptr.next != None:
            this_val = ptr.val
            next_val = ptr.next.val
            com_divisor = self._find_common_divisor(this_val, next_val)
            new_node = ListNode(com_divisor, None)
            
            all_nodes.append(ptr)
            all_nodes.append(new_node)
            ptr = ptr.next
        
        all_nodes.append(ptr)

        for i in range(len(all_nodes) - 1):
            all_nodes[i].next = all_nodes[i+1]
        return all_nodes[0]