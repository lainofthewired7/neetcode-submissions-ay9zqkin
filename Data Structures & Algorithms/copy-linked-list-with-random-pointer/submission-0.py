class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        curr = head

        myDict = {}

        while curr:

            myDict[curr] = Node(curr.val)

            curr = curr.next

        dummyNode = Node(0)

        curr = head

        dummyCurr = dummyNode

        while curr:

            dummyCurr.next = myDict[curr]

            dummyCurr = dummyCurr.next

            if curr.random:

                dummyCurr.random = myDict[curr.random]

            curr = curr.next

        return dummyNode.next