# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        counter=0
        heap=[]
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, counter, lists[i]))
                counter+=1
        dummy=ListNode(-1)
        curr=dummy
        while heap:
            val, _, node=heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter+=1
            curr.next=node
            curr=curr.next
        return dummy.next