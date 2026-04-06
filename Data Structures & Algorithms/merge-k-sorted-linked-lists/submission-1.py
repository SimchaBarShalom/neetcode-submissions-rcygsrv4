# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap_min=[]
        for i in range (len(lists)):
            node=lists[i]
            if node:
                heapq.heappush(heap_min,(node.val,i,node))
        
        dummy=ListNode(0)
        tail=dummy
        while len(heap_min)>0:
            val,i,node=heapq.heappop(heap_min)  
            tail.next=node
            tail=tail.next
            if node.next!=None:
                heapq.heappush(heap_min,(node.next.val,i,node.next))        
        return dummy.next
        