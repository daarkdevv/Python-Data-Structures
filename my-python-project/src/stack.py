class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.height = 0

    def Push(self, value):
        newNode = Node(value)
        
        if self.height == 0:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        
        self.height += 1

    def Pop(self):
        if self.height == 0:
            return None
        
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp.value

    def Peek(self):
        if self.height == 0:
            return None
        return self.top.value

    def isEmpty(self):
        return self.height == 0

    def Print(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
