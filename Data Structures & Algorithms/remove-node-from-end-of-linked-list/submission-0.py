# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head

        prev = ListNode(None, head)

        prev.next = head

        index = 0
        
        length = 0

        while curr:

            length += 1

            curr = curr.next

        curr = head

        target = length - n

        if target == 0:

            return head.next


        while curr:

            if index == target:

                prev.next = curr.next

                return head
            
            curr = curr.next

            prev = prev.next

            index += 1






        

        



        