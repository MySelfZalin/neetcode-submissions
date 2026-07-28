# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        remain = 0 
        
        while l1 or l2 or remain:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            curr_value = val1 + val2 + remain
            remain = curr_value // 10
            finish_value = curr_value % 10

            if l1:
                l1.val = finish_value
                prev.next = l1
            elif l2:
                l2.val = finish_value
                prev.next = l2
            else:
                prev.next = ListNode(val=finish_value)    

            if l1: l1 = l1.next
            if l2: l2 = l2.next
            prev = prev.next

        return dummy.next                 
        