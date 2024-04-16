class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def is_empty1(self):
        return self.head is None
    def add1(self, item):
        if self.head is None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next
    def pop1(self):
        if self.head:
            item = self.head
            self.head = self.head.next
            return item
        raise ValueError('Queue is empty.')
    @property
    def peek1(self):
        return self.head.item
    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
    def __str__(self):
        s = ''
        current = self.head
        while current is not None:
            s += str(current.item)+' '
            current = current.next
        return f'start -> {s}<- end'
class MyStack:
    def __init__(self):
        self.rtype1=Queue()
        self.rtype2=Queue()
    def push(self, x: int) -> None:
        self.rtype1.add1(x)
    def pop(self) -> int:
        if len(self.rtype1)==0:
            return -1
        while len(self.rtype1)!=1:
            val = self.rtype1.pop1()
            self.rtype2.add1(val)
        a=self.rtype1.peek1
        self.rtype1=Queue()
        while len(self.rtype2):
            val = self.rtype2.pop1()
            self.rtype1.add1(val)
        while not isinstance(a,int):
            a=a.item
        return a
    def top(self) -> int:
        print(str(self.rtype1))
        if len(self.rtype1)==0:
            return -1
        while len(self.rtype1):
            val = self.rtype1.pop1()
            self.rtype2.add1(val)
        while len(self.rtype2):
            val = self.rtype2.pop1()
            self.rtype1.add1(val)
        while not isinstance(val.item,int):
            val=val.item
        return val.item
    def empty(self) -> bool:
        return len(self.rtype1)==0
