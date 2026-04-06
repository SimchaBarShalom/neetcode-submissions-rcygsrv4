# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i=head
        step=n
        while step>0 and i:
            i=i.next
            step-=1
        j=head
        if not i:
            return head.next
        while i.next:
            i=i.next
            j=j.next
        j.next=j.next.next
        return head

        


        