class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def Enqueue(self, value):
        newNode = Node(value)
        
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        
        self.length += 1

    def Dequeue(self):
        if self.length == 0:
            return None
        
        temp = self.first
        
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
        
        temp.next = None
        self.length -= 1
        return temp.value

    def Peek(self):
        if self.length == 0:
            return None
        return self.first.value

    def isEmpty(self):
        return self.length == 0

    def Print(self):
        temp = self.first
        while temp is not None:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")
