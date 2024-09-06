# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        # Initial idea is to use a FIFO queue and append the pointer to queue if val is NOT 
        pointer = head

        keep = []

        unique_nums = set(nums)  # A test case will timeout if not using set.

        while pointer != None:
            if pointer.val not in unique_nums:
                keep.append(pointer)
            pointer = pointer.next

        new_head = keep[0]
        for i in range(0, len(keep) - 1):
            keep[i].next = keep[i+1]
        
        keep[-1].next = None
        
        return new_head