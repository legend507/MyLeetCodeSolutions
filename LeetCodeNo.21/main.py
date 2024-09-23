# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Put everything in a list, then create a linked list out of the list.
        store = []
        ptr1 = list1
        while ptr1 != None:
            store.append(ptr1.val)
            ptr1 = ptr1.next
        ptr2 = list2
        while ptr2 != None:
            store.append(ptr2.val)
            ptr2 = ptr2.next
        
        store.sort()

        if len(store) == 0:
            return None

        ret = ListNode(store[0])
        ptr = ret
        for i in range(1, len(store)):
            ptr.next = ListNode(store[i])
            ptr = ptr.next
        return ret

