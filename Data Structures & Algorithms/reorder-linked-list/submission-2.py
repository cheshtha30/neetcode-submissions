# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow  = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        #Split
        second = slow.next
        slow.next = None

        #reverse second part 
        prev = None 
        curr = second 

        while curr:
            NextNode = curr.next
            curr.next = prev
            prev = curr
            curr = NextNode

        second = prev

        #merge 

        first = head 

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

