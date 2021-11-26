class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head #Initialising both fast and slow to head
        
        for i in range(n):
            fast = fast.next #we are making Fast to point to the node which is right next to the node which is to be removed
        
        if fast is None: 
            return head.next 
        
        while fast.next:
            fast = fast.next #After this we are increasing both fast and head by 1 step each
            slow = slow.next
        
        #when fast reaches end of the list, slow points to the node behind the target, so we skip the target and move to next of target

        slow.next = slow.next.next 
        return head