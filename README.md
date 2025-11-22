# DSA Project - Data Structures Implementation

This project contains implementations of fundamental data structures in Python, useful for understanding how these structures work at a low level.

## Structures Included

### 1. **Singly Linked List** (`src/main.py`)
A linear data structure with nodes containing a value and a reference to the next node.

**Operations:**
- `AddLast(value)` - Add element at the end
- `AddFirst(value)` - Add element at the beginning
- `Pop()` - Remove and return the last element
- `PopFirst()` - Remove and return the first element
- `get(index)` - Retrieve node at specific index
- `Set(index, value)` - Update value at specific index
- `Insert(index, value)` - Insert element at specific index
- `Remove(index)` - Remove element at specific index
- `Reverse()` - Reverse the linked list
- `findMiddle()` - Find the middle element using two-pointer approach
- `PrintList()` - Print all elements

### 2. **Doubly Linked List** (`src/doubly_linked_list.py`)
A linear data structure with nodes containing a value, reference to the next node, and reference to the previous node.

**Operations:**
- `AddLast(value)` - Add element at the end
- `AddFirst(value)` - Add element at the beginning
- `Pop()` - Remove and return the last element
- `PopFirst()` - Remove and return the first element
- `get(index)` - Retrieve node at specific index (optimized traversal)
- `Set(index, value)` - Update value at specific index
- `Insert(index, value)` - Insert element at specific index
- `Remove(index)` - Remove element at specific index
- `PrintList()` - Print forward traversal
- `PrintListReverse()` - Print backward traversal

### 3. **Stack** (`src/stack.py`)
A Last-In-First-Out (LIFO) data structure.

**Operations:**
- `Push(value)` - Add element to the top
- `Pop()` - Remove and return the top element
- `Peek()` - View the top element without removing
- `isEmpty()` - Check if stack is empty
- `Print()` - Print all elements

### 4. **Queue** (`src/queue.py`)
A First-In-First-Out (FIFO) data structure.

**Operations:**
- `Enqueue(value)` - Add element to the rear
- `Dequeue()` - Remove and return the front element
- `Peek()` - View the front element without removing
- `isEmpty()` - Check if queue is empty
- `Print()` - Print all elements

## Project Structure

```
my-python-project/
├── README.md
└── src/
    ├── main.py                  # Singly Linked List implementation
    ├── doubly_linked_list.py    # Doubly Linked List implementation
    ├── stack.py                 # Stack implementation
    └── queue.py                 # Queue implementation
```

## Usage Examples

### Singly Linked List
```python
from src.main import LinkedList

ll = LinkedList(0)
ll.AddLast(1)
ll.AddLast(2)
ll.AddLast(3)
ll.PrintList()
middle = ll.findMiddle()
```

### Doubly Linked List
```python
from src.doubly_linked_list import DoublyLinkedList

dll = DoublyLinkedList(1)
dll.AddLast(2)
dll.AddLast(3)
dll.PrintList()
dll.PrintListReverse()
```

### Stack
```python
from src.stack import Stack

stack = Stack()
stack.Push(10)
stack.Push(20)
stack.Push(30)
stack.Print()
value = stack.Pop()
```

### Queue
```python
from src.queue import Queue

queue = Queue()
queue.Enqueue(1)
queue.Enqueue(2)
queue.Enqueue(3)
queue.Print()
value = queue.Dequeue()
```

## Time Complexity

| Operation | Singly LL | Doubly LL | Stack | Queue |
|-----------|-----------|-----------|-------|-------|
| Access    | O(n)      | O(n)      | O(n)  | O(n)  |
| Insert    | O(n)      | O(n)      | O(1)  | O(1)  |
| Delete    | O(n)      | O(n)      | O(1)  | O(1)  |
| Search    | O(n)      | O(n)      | O(n)  | O(n)  |

## Space Complexity
All implementations have O(n) space complexity where n is the number of elements.

## Notes
- These implementations use node-based structures to demonstrate how these data structures work internally
- Doubly Linked List provides optimized traversal by choosing the shorter path from either end
- Stack and Queue are fundamental for algorithm problems like expression evaluation, BFS, DFS, etc.
