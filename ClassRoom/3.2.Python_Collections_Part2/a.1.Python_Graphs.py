# Basic Graph in Python using an adjacency list
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def print_graph(self):
        for node in self.graph:
            for neighbor in self.graph[node]:
                print(f"{node} -> {neighbor}", end=' ')
            print()

# Usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.print_graph()


## Stack in details
# Expanded Stack Example in Python

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("peek from empty stack")
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

# Usage
stack = Stack()
stack.push('a')
stack.push('b')
print(stack.peek())  # Output: 'b', peek at the top item
print(stack.size())  # Output: 2, get the size of the stack
stack.pop()          # Removing 'b'
print(stack.is_empty())  # Output: False, check if stack is empty


## Queues in Details
# Expanded Queue Example in Python

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        raise IndexError("dequeue from empty queue")
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

# Usage
queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
print(queue.size())  # Output: 2
queue.dequeue()      # Removing 'a'
print(queue.is_empty())  # Output: False

## LinkedLists in Details
# Expanded Linked List Example in Python

# Node class for a Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """ Append an item to the end of the list """
        if not self.head:
            self.head = Node(data)
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = Node(data)

    def insert(self, data, position):
        """ Insert an item at the given position """
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        previous = None
        count = 0
        while current and count < position:
            previous = current
            current = current.next
            count += 1
        if previous is None:
            raise IndexError("Position out of bounds")
        previous.next = new_node
        new_node.next = current

    def delete(self, key):
        """ Delete the first occurrence of an item with the given value """
        current = self.head
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next
        if current is None:  # Item not found
            return
        if previous is None:  # Item is the head
            self.head = current.next
        else:  # Item is in the middle or end
            previous.next = current.next

    def print_list(self):
        """ Print the list """
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

# Example usage
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.insert(4, 2)  # Insert 4 at position 2
llist.delete(2)     # Delete the first occurrence of 2
llist.print_list()  # Output: 1 4 3



## Trees in Details
# Expanded Tree Example in Python

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(TreeNode(child_node))

    def print_tree(self):
        print(self.data)
        for child in self.children:
            child.print_tree()

    def traverse_preorder(self):
        print(self.data, end=' ')
        for child in self.children:
            child.traverse_preorder()

# Usage
root = TreeNode('Root')
child1 = TreeNode('Child1')
child2 = TreeNode('Child2')
root.children.append(child1)
root.children.append(child2)
child1.add_child('Grandchild1')
root.traverse_preorder()  # Pre-order traversal: Root -> Child1 ->
