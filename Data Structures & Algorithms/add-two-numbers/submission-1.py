# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        num1 = []

        num2 = []

        curr1 = l1

        curr2 = l2

        while curr1:

            num1.append(curr1.val)

            curr1 = curr1.next

        while curr2:

            num2.append(curr2.val)

            curr2 = curr2.next

        num1 = num1[::-1]

        num2 = num2[::-1]

        print(num1)

        print(num2)

        int1 = "".join(map(str, num1))

        int2 = "".join(map(str, num2))

        print(int1)

        print(int2)

        int1 = int(int1)

        int2 = int(int2)

        final = int1 + int2

        final = str(final)

        print(final)

        dummyNode = ListNode(0)

        curr = dummyNode

        for i in range(len(final)-1, -1, -1):

            curr.next = ListNode(final[i])

            curr = curr.next

        return dummyNode.next

            


            

            

        
        





        

        
        