# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        store = []

        curr1 = list1

        curr2 = list2

        while curr1:

            store.append(curr1.val)

            curr1 = curr1.next

        while curr2:

            store.append(curr2.val)

            curr2 = curr2.next

        store.sort()

        dummy = ListNode()

        curr = dummy

        for val in store:

            curr.next = ListNode(val)

            curr = curr.next

        return dummy.next


