class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def AddLast(self, value):
        newNode = Node(value)
        
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.length = 1
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.length += 1

    def AddFirst(self, value):
        newNode = Node(value)
        
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.length = 1
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            self.length += 1

    def Pop(self):
        if self.head is None:
            return None
        
        if self.head == self.tail:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp.value
        
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1
        return temp.value

    def PopFirst(self):
        if self.head is None:
            return None
        
        if self.head == self.tail:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp.value
        
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1
        return temp.value

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index < self.length / 2:
            temp = self.head
            for i in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for i in range(self.length - 1, index, -1):
                temp = temp.prev
        
        return temp

    def Set(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value

    def Insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        
        if index == 0:
            self.AddFirst(value)
            return
        
        if index == self.length:
            self.AddLast(value)
            return
        
        newNode = Node(value)
        temp = self.get(index - 1)
        
        newNode.next = temp.next
        newNode.prev = temp
        temp.next.prev = newNode
        temp.next = newNode
        self.length += 1

    def Remove(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.PopFirst()
        
        if index == self.length - 1:
            return self.Pop()
        
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        self.length -= 1
        return temp.value

    def PrintList(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" <-> ")
            temp = temp.next
        print("None")

    def PrintListReverse(self):
        temp = self.tail
        while temp is not None:
            print(temp.value, end=" <-> ")
            temp = temp.prev
        print("None")
