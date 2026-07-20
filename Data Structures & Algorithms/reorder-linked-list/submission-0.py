# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# [0,1,2,3,4,5,6]
#  f = head , slow = head
#slow = slow .next , fast = fast.next.next till fast reach end
# where we get slow last is the point of split 
#from split.next is second sep 
# 0 -> 1->2->3-> 4->5 ->6
#      s  f
#         s       f
#             s          f    done 
# 0->1->2->3->None       4->5->6->None

# reverse second  6->5->4->None
#Merge  0->6->1->5->2->4->3

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow , fast  = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        #split
        second = slow.next 
        slow.next = None 
        
        #reverse second half 
        curr = second
        prev = None 
       
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






        



        