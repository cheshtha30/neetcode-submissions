# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        for _ in range(n):
            fast = fast.next

        if fast == None:
            return head.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head
        # length = 0
        # temp = head
        # while temp :
        #     length +=1
        #     temp = temp.next

        # if length == n:
        #     new_head = head.next
        #     del head
        #     return new_head

        # pos_to_stop = length - n -1
        # temp = head
        # count =  0
        # while count < pos_to_stop:
        #     count += 1
        #     temp = temp.next
        # temp.next = temp.next.next

        # return head

        

        


