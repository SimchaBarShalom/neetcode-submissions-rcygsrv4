# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i=head
        j=head
        while j and j.next:
            i=i.next
            j=j.next.next
            if i==j:
                return True
        return False