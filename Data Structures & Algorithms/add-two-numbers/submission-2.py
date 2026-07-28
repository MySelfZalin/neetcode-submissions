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
        
        while l1 and l2:
            curr_value = l1.val + l2.val + remain
            l1.val = curr_value % 10
            remain = curr_value // 10
            prev.next = l1
            l1 = l1.next
            l2 = l2.next
            prev = prev.next


        curr = l1 if l1 else l2
        prev.next = curr
        
        while curr and remain:
                curr_value = curr.val + remain
                curr.val = curr_value % 10
                remain = curr_value // 10
                prev = curr
                curr = curr.next

        if remain:
            prev.next = ListNode(val=remain)

        return dummy.next    