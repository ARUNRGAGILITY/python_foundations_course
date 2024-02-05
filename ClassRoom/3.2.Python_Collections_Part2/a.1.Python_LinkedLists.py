# Linked List in Python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = Node(data)

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()

# Usage
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.print_list()  # Output: 1 2 3


# Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """ Append a node with the specified data to the end of the list """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data, position):
        """ Insert a node with the specified data at the specified position """
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        prev_node = self.head
        for i in range(position - 1):
            prev_node = prev_node.next
            if prev_node is None:
                raise Exception("Position out of bounds")
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete(self, key):
        """ Delete the first node with the specified data """
        current_node = self.head
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return  # The data not found
        if prev_node is None:
            self.head = current_node.next
        else:
            prev_node.next = current_node.next

    def delete_at_position(self, position):
        """ Delete the node at the specified position """
        if self.head is None:
            return
        current_node = self.head
        if position == 0:
            self.head = current_node.next
            return
        for i in range(position - 1):
            current_node = current_node.next
            if current_node.next is None:
                raise Exception("Position out of bounds")
        current_node.next = current_node.next.next

    def search(self, key):
        """ Search for the first node with the specified data and return its position """
        current_node = self.head
        position = 0
        while current_node:
            if current_node.data == key:
                return position
            current_node = current_node.next
            position += 1
        return -1  # Data not found

    def print_list(self):
        """ Print all the elements of the list """
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Usage example
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.insert(4, 2)  # Insert 4 at position 2 (after 2)
sll.print_list()  # Output: 1 -> 2 -> 4 -> 3 -> None

sll.delete(2)     # Delete the node with data 2
sll.print_list()  # Output: 1 -> 4 -> 3 -> None

sll.delete_at_position(1)  # Delete the node at position 1 (which has data 4)
sll.print_list()  # Output: 1 -> 3 -> None

position = sll.search(3)  # Search for data 3
print(f"Element 3 found at position: {position}")  # Output: Element 3 found at position: 1

'''
Singly Linked List Summary:
The Node class represents an element in the list with data and a reference to the next node.
The SinglyLinkedList class manages the list, keeping a reference to the head node.
The append method adds a node to the end of the list.
The insert method inserts a node at a given position.
The delete method removes a node with a specified value.
The delete_at_position method removes a node at a specified position.
The search method finds the position of the node with the specified value.
The print_list method displays all the elements in the list.
'''

# Doubly Linked List
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """ Append a node with the specified data to the end of the list """
        if not self.head:
            self.head = DoublyNode(data)
            return
        current = self.head
        while current.next:
            current = current.next
        new_node = DoublyNode(data)
        current.next = new_node
        new_node.prev = current

    def prepend(self, data):
        """ Prepend a node with the specified data to the beginning of the list """
        new_node = DoublyNode(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insert_after(self, key, data):
        """ Insert a new node after the specified key """
        current = self.head
        while current and current.data != key:
            current = current.next
        if current is None:
            return
        new_node = DoublyNode(data)
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def delete(self, key):
        """ Delete a node by the specified key """
        current = self.head
        while current and current.data != key:
            current = current.next
        if current is None:
            return  # Key not found
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        if current == self.head:  # If it's the head node
            self.head = current.next

    def print_list(self):
        """ Print all the elements of the list """
        current = self.head
        while current:
            print(current.data, end=" <=> ")
            current = current.next
        print("None")

# Usage Example
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.prepend(0)  # Add 0 at the beginning
dll.print_list()  # Output: 0 <=> 1 <=> 2 <=> 3 <=> None

dll.insert_after(1, 1.5)  # Insert 1.5 after 1
dll.print_list()  # Output: 0 <=> 1 <=> 1.5 <=> 2 <=> 3 <=> None

dll.delete(2)  # Delete node with data 2
dll.print_list()  # Output: 0 <=> 1 <=> 1.5 <=> 3 <=> None

# Circular Linked List

class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """ Append a node with the specified data to the end of the list """
        if not self.head:
            self.head = CircularNode(data)
            self.head.next = self.head
            return
        new_node = CircularNode(data)
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def prepend(self, data):
        """ Prepend a node with the specified data to the beginning of the list """
        new_node = CircularNode(data)
        current = self.head
        new_node.next = self.head
        if not self.head:
            new_node.next = new_node
        else:
            while current.next != self.head:
                current = current.next
            current.next = new_node
        self.head = new_node

    def delete(self, key):
        """ Delete a node by the specified key """
        if self.head is None:
            return
        current = self.head
        prev = None
        while current.next != self.head:
            if current.data == key:
                if prev:
                    prev.next = current.next
                else:
                    if current.next == self.head:  # Single element
                        self.head = None
                    else:
                        self.head = current.next
                        tail = self.head
                        while tail.next != current:
                            tail = tail.next
                        tail.next = self.head
                return
            prev = current
            current = current.next
        if current.data == key:
            if prev:
                prev.next = self.head
            else:
                self.head = None

    def print_list(self):
        """ Print all the elements of the list """
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print()

# Usage Example
circular_list = CircularLinkedList()
circular_list.append(1)
circular_list.append(2)
circular_list.append(3)
circular_list.prepend(0)  # Add 0 at the beginning
circular_list.print_list()  # Output: 0 -> 1 -> 2 -> 3 ->

circular_list.delete(2)  # Delete node with data 2
circular_list.print_list()  # Output: 0 -> 1 -> 3 ->

# Circular Doubly Linked List

class CircularDoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """ Append a node with the specified data to the end of the list """
        if not self.head:
            self.head = CircularDoublyNode(data)
            self.head.next = self.head
            self.head.prev = self.head
            return
        new_node = CircularDoublyNode(data)
        tail = self.head.prev
        tail.next = new_node
        new_node.prev = tail
        new_node.next = self.head
        self.head.prev = new_node

    def prepend(self, data):
        """ Prepend a node with the specified data to the beginning of the list """
        self.append(data)  # Reuse append to add to the end
        self.head = self.head.prev  # Update head to the new node

    def delete(self, key):
        """ Delete a node by the specified key """
        if self.head is None:
            return
        current = self.head
        while True:
            if current.data == key:
                if current.next == current:  # Single element
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.head:
                        self.head = current.next
                return
            current = current.next
            if current == self.head:
                break  # Key not found, end loop

    def print_list(self):
        """ Print all the elements of the list """
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" <=> ")
            current = current.next
            if current == self.head:
                break
        print("HEAD")

# Usage Example
cdll = CircularDoublyLinkedList()
cdll.append(1)
cdll.append(2)
cdll.append(3)
cdll.prepend(0)  # Add 0 at the beginning
cdll.print_list()  # Output: 0 <=> 1 <=> 2 <=> 3 <=> HEAD

cdll.delete(2)  # Delete node with data 2
cdll.print_list()  # Output: 0 <=> 1 <=> 3 <=> HEAD
