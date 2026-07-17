# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        0, 1, 2, 3
        6, 5, 4

        0, 1, 2, 3
        7, 6, 5, 4

        dummy = ListNode(next=head)

        fast = slow = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


       
        current = slow.next
        slow.next = None

        prev = None
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode

        firstNode = head
        secondNode = prev
        while secondNode:
            next_first = firstNode.next
            next_second = secondNode.next

            firstNode.next = secondNode
            secondNode.next = next_first

            firstNode = next_first
            secondNode = next_second
            



        