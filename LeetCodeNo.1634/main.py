# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        pointer = poly1
        poly1_dict = {}
        while pointer != None:
            poly1_dict[pointer.power] = pointer.coefficient
            pointer = pointer.next
        
        pointer = poly2
        poly2_dict = {}
        while pointer != None:
            poly2_dict[pointer.power] = pointer.coefficient
            pointer = pointer.next
        
        for power, _ in poly2_dict.items():
            if power in poly1_dict:
                poly1_dict[power] += poly2_dict[power]
            else:
                poly1_dict[power] = poly2_dict[power]
        
        ret_list = []

        # Make sure the power (key in poly1_dict) is desceding.
        poly1_dict_ordered = dict(sorted(poly1_dict.items(), key=lambda item: item[0], reverse=True))

        for power, coefficient in poly1_dict_ordered.items():
            if coefficient != 0:
                ret_list.append(PolyNode(x = coefficient, y = power, next = None))
        if len(ret_list) == 0:
            return None

        head = ret_list[0]
        for i in range(len(ret_list) - 1):
            ret_list[i].next = ret_list[i+1]
        return head
