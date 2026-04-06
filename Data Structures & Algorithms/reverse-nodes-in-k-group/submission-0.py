# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverseK(head: ListNode, k: int) -> ListNode:
            prev = None
            curr = head
            while k > 0:
                next_ptr = curr.next
                curr.next = prev
                prev = curr
                curr = next_ptr
                k -= 1
            return prev  

        dummy = ListNode(0, head)
        prev = dummy

        while True:
            curr_kth = prev
            for i in range(k):
                curr_kth = curr_kth.next
                if not curr_kth:
                    return dummy.next

            next_k = curr_kth.next
            curr = prev.next     

            curr_head = reverseK(curr, k)

            prev.next = curr_head     
            curr.next = next_k     

            prev = curr
        