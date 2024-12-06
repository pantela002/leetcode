class Node:
    def __init__(self,val,next_node=None,prev_node=None):
        self.val=val
        self.next=next_node
        self.prev=prev_node

class MyLinkedList:
    def __init__(self):
        self.head, self.tail = None, None

    def get(self, index: int) -> int:
        if not self.head:
            return -1

        tmp = self.head
        while index>0:
            if not tmp:
                return -1
            tmp=tmp.next
            index-=1
        return tmp.val if tmp else -1

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            self.tail= self.head
            return
        
        tmp = Node(val)
        tmp.next = self.head
        self.head.prev = tmp
        self.head = self.head.prev

    def addAtTail(self, val: int) -> None:
        if not self.tail:
            self.head = Node(val)
            self.tail= self.head
            return  None
        
        tmp = Node(val)
        tmp.prev = self.tail
        self.tail.next = tmp
        self.tail = self.tail.next

    def addAtIndex(self, index: int, val: int) -> None:
        if not self.tail:
            if index == 0:
                self.head = Node(val)
                self.tail= self.head
            return None
        
        pom = self.head
        while index>0:
            if not pom:
                return None
            pom=pom.next
            index-=1

        if not pom:
            tmp = Node(val)
            tmp.prev = self.tail
            self.tail.next = tmp
            self.tail = self.tail.next
            return None
        
        tmp = Node(val)
        tmp.prev = pom.prev
        tmp.next = pom
        if tmp.prev:
            tmp.prev.next = tmp
            tmp.next.prev = tmp
        else:
            tmp.next.prev = tmp
            self.head = self.head.prev

        
    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return None
        
        pom = self.head
        while index>0:
            pom = pom.next
            index-=1
            if not pom:
                return None
        
        if pom == self.head and pom == self.tail:
            self.head=None
        elif pom == self.head:
            self.head = self.head.next
            self.head.prev = None
        elif pom == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            pom.prev.next = pom.next
            pom.next.prev = pom.prev
        
        
            



      


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
