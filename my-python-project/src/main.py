head = {
    "value": 1,
    "next": {
        "value": 2,
        "next": {
            "value": 3,
            "next": {
                "value": 4,
                "next": {}
            }
        }
    }
}

# print(head['next'] ['next'] ['value'])

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.tail = newNode
        self.head = newNode
        self.length = 1
        

    def Check_TailHead(self, node):
        
        if self.length != 0:
            return
        
        self.head = node  # Assign the node to head
        self.tail = node  # Assign the node to tail
        self.length += 1
        
    def AddLast(self , value):
        newNode = Node(value)
        
        if self.head is None:
           self.Check_TailHead(newNode)
        else:
            self.tail.next = newNode
            self.tail = newNode
        
        self.length += 1       
        
    def AddFirst(self,value):
        newNode = Node(value)
        
        if self.head is None:
           self.Check_TailHead(newNode)
        else:
            newNode.next = self.head
            self.head = newNode
            length += 1
    
    def Pop(self):
        temp = self.head
        
        if(self.head is None):
            return None
        if(self.head == self.tail):
            self.head = None
            self.tail = None
        else:
            while temp is not None:
                if(temp.next == self.tail):
                    self.tail = temp
                    temp.next = None
                    break
                else:
                  temp = temp.next     
                
        self.length -= 1
        return temp.value
            

    
    def PopFirst(self):
        if self.head is None:
            return None
        
        temp = self.head
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:    
          self.head = self.head.next   
       
        
        temp.next = None
        self.length -= 1
        return temp
        
    
    def get(self , index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        
        for i in range(index):
            temp = temp.next
            
        return temp
    
    def Set(self , index , value):
        temp = self.get(index)
        
        if temp is not None:    
            temp.value = value
            
            
    def Insert(self,index , value):
        
        if index < 0 or index >= self.length:
            return None
   
        temp = self.get(index - 1)
            
        if index == 0:
          return  self.AddFirst(value)
            
        if index == self.length:
         return  self.AddLast(value)
                
        newNode = Node(value) 
        
        newNode.next = temp.next
        temp.next = newNode
       
        self.length += 1
    
    def PrintList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def Remove(self,index):
        if index < 0 or index >= self.length:
            return None
        
        if(index == 0):
            return self.PopFirst()
        elif(index == self.length - 1):
            return self.Pop()

        prev = self.get(index - 1)  
        removednode = prev.next
        prev.next = removednode.next
        removednode.next = None
        
        self.length -= 1
        
    def Reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for i in range(self.length):
            after = temp.next
            temp.next = before
            temp = after
    
    
    
    
    def findMiddle(self):
        temp = self.head
        temp2 = self.head
        
        
        if(self.head is None):
            return
        
        while temp2 and temp2.next:       
            temp = temp.next
            temp2 = temp2.next.next
        
        return temp.value    
                                            
    

ll = LinkedList(0)
ll.AddLast(1)
ll.AddLast(2)
ll.AddLast(3)
ll.AddLast(3)
ll.AddLast(55)
ll.AddLast(233)



print(ll.findMiddle())
        
        
        