# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast=head, head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        first, second=head, slow.next
        slow.next=None
        prev, curr=None, second
        while curr:
            nextNode=curr.next
            curr.next=prev
            prev=curr
            curr=nextNode
        second=prev
        while second:
            firstNext=first.next
            secondNext=second.next
            first.next=second
            second.next=firstNext
            first=firstNext
            second=secondNext