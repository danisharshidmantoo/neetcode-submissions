class ListNode:
    def __init__(self,val,next_node=None):
        self.val = val
        self.next = next_node
class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
    
    def get(self, index: int) -> int:
        dummy = self.head
        idx = -1
        while idx<index and dummy.next:
            dummy = dummy.next
            idx += 1
        if idx!=index:
            return -1
        return dummy.val

    def insertHead(self, val: int) -> None:
        temp = self.head.next
        self.head.next = ListNode(val,temp)

    def insertTail(self, val: int) -> None:
        #first go to the tail and then insert there
        dummy = self.head
        while dummy.next:
            dummy = dummy.next
        dummy.next = ListNode(val)
        

    def remove(self, index: int) -> bool:
        dummy = self.head
        idx = -1
        while idx<index-1 and dummy:
            dummy = dummy.next
            idx += 1
        if idx != index-1 or not dummy:
            return False
        cur = dummy.next
        if cur:
            dummy.next = cur.next
        else:
            return False
        return True

    def getValues(self) -> List[int]:
        values = []
        dummy = self.head.next
        while dummy:
            values.append(dummy.val)
            dummy = dummy.next
        return values
