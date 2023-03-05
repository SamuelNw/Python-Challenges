# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        """
        # Initiate the resulting linked list with a dummy.
        # Handle lower constraints:
            - If all linked lists are empty, retrn an empty arr.
            - If one of the two lists is empty, return the head of the other.
        # With both lists populated, use list1 and list2 pointers to 
        repeatedly check the smaller val then add that node to be the head
        of the result.
        
        """
        current = dummy = ListNode()

        # if not list1 and not list2:
        #     return dummy.next

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
                current = current.next
            else:
                current.next = list2
                list2 = list2.next
                current = current.next

        if not list1 or not list2:
            current.next = list1 if list1 else list2

        return dummy.next
