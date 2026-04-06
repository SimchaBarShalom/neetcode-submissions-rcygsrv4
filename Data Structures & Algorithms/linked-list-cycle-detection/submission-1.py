# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        start=head
        end=head
        while end and end.next:
            start=start.next
            end=end.next.next
            if start==end:
                return True
        return False