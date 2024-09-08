# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _break_up(self, head, length):
        new_head = head

        for _ in range(length - 1):
            new_head = new_head.next

        if new_head != None:
            ret = new_head.next
            new_head.next = None
            return ret
        else:
            return None

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Initial thouhgs: 1. get length of linked list, find out where to break.

        # Corner case k = 1
        if k == 1:
            return [head]

        count = 0
        pointer = head
        while pointer != None:
            pointer = pointer.next
            count += 1

        pointer = head
        ret = []
        # If k > count, then break to every single element and append None.
        if k >= count:
            
            for i in range(k):
                if pointer != None:
                    ret.append(pointer)
                    pointer = pointer.next
                    ret[-1].next = None
                else:
                    ret.append(None)

        else:
            each_part = count // k
            mode = count % k

            length_each_part = [each_part] * k
            # Distribute mode to each part

            for i in range(k):
                if mode != 0:
                    length_each_part[i] += 1
                    mode -= 1

            for i in length_each_part:
                ret.append(pointer)
                pointer = self._break_up(pointer, i)
        
        return ret
