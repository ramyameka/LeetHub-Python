'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = list1
        c2 = list2
        while((c2 is not None) and (c1 is not None)):
            val1 = c2.val
            val2 = c2.next.val
            if c1.val <= val1 and c1.val <= val2:
                ref1 = c1.next
                ref2 = c2.next
                c2.next = c1
                c2.next.next = ref2
                c1 = ref1

            c2 = c2.next

        return list2
