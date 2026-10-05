# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(-1, head)
        grpPrev=dummy

        def getKth(curr, k):
            while curr and k>0:
                curr=curr.next
                k-=1
            return curr

        while True:
            kth=getKth(grpPrev, k)
            if not kth:
                break
            grpNext=kth.next
            prev, curr=kth.next, grpPrev.next
            while curr!=grpNext:
                nextNode=curr.next
                curr.next=prev
                prev=curr
                curr=nextNode
            temp=grpPrev.next
            grpPrev.next=kth
            grpPrev=temp
        return dummy.next