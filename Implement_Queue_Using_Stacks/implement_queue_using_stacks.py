class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next
class Stack:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def push1(self, item):
        self.head = Node(item, self.head)
    def pop1(self):
        item = self.head.item
        self.head = self.head.next
        return item
    @property
    def peek1(self):
        return self.head.item
    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count +=1
            current = current.next
        return count
    def __str__(self):
        s = ''
        cur = self.head
        while cur is not None:
            s = str(cur.item) + ' ' +s
            cur = cur.next
        return 'bottom -> '+ s+'<- top'
class MyQueue:
    def __init__(self):
        self.rtype1=Stack()
        self.rtype2=Stack()
    def push(self, x: int) -> None:
        self.rtype1.push1(x)
    def pop(self) -> int:
        if len(self.rtype1)==0:
            return -1
        while len(self.rtype1):
            val = self.rtype1.pop1()
            self.rtype2.push1(val)
        a=self.rtype2.pop1()
        while len(self.rtype2):
            val = self.rtype2.pop1()
            self.rtype1.push1(val)
        return a 
    def peek(self) -> int:
        if len(self.rtype1)==0:
            return -1
        while len(self.rtype1):
            val = self.rtype1.pop1()
            self.rtype2.push1(val)
        a=self.rtype2.peek1
        while len(self.rtype2):
            val = self.rtype2.pop1()
            self.rtype1.push1(val)
        return a
    def empty(self) -> bool:
        return len(self.rtype1)==0
