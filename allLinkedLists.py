"""
Structure of comments:
Function description.
Time complexity O()
"""


#Singly Linked List Node class - Represents a single node in a singly linked list.
class Node:
    #Initializes the node with data and a reference to the next node.
    #Time complexity: O(1)
    def __init__(self, data):
        self.data = data
        self.next = None

class NodeWithPrev(Node):
    #Creates a node with an extra previous-pointer reference for doubly linked lists.
    #Time complexity: O(1)
    def __init__(self, data):
        self.prev = None
        super().__init__(data)


#LinkedLists parent class - Base class for singly linked list implementations (with and without tail).
class LinkedLists:
    #Initializes an empty linked list with head pointer set to None and size counter set to 0.
    #Time complexity: O(1)
    def __init__(self):
        self.head = None
        self.size = 0


#Singly Linked List with Tail - Efficient implementation with direct access to both head and tail.
class SinglyLinkedList(LinkedLists):
    #Initializes an empty singly linked list with head and tail pointers set to None.
    #Time complexity: O(1)
    def __init__(self):
        self.tail = None
        super().__init__()

    #Returns the number of elements currently in the linked list.
    #Time complexity: O(1)
    def __len__(self): return self.size

    #Loops throgh items of the linked list
    #Time complexity: O(n)
    def __iter__(self):
        items = []

        curr = self.head
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next

        return items

    #Returns a string representation of the linked list showing all elements from head to tail.
    #Time complexity: O(n), where n is the number of elements in the list.
    def __repr__(self):
        if self.is_empty(): return "[]"

        items = []
        curr = self.head
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next
        items.append("None")

        return "->".join(items)

    #Checks if an item exists in the linked list. Raises ValueError if list is empty.
    #Time complexity: O(n), where n is the number of elements in the list.
    def __contains__(self, item):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        while curr is not None:
            if curr.data == item: return True
            curr = curr.next

        return False

    #Adds an element to the end of the linked list.
    #Time complexity: O(1)
    def append(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    #Adds an element to the beginning of the linked list.
    #Time complexity: O(1)
    def prepend(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    #Inserts an element at the specified index position. Raises ValueError if index is out of range.
    #Time complexity: O(n), where n is the index position.
    def insert(self, value, index):
        if index < 0: raise ValueError("Index out of range!")

        if index == 0:
            self.prepend(value)
            return
        
        if self.is_empty(): raise ValueError("Empty List!")

        new_node = Node(value)

        curr = self.head
        for _ in range(index - 1):
            if curr.next is None: raise ValueError("Index out of range!")
            curr = curr.next

        new_node.next = curr.next
        curr.next = new_node

        if new_node.next is None: self.tail = new_node
        self.size += 1

    #Removes the first occurrence of an element with the specified value. Raises ValueError if list is empty.
    #Time complexity: O(n), where n is the number of elements in the list.
    def remove(self, value):
        if self.is_empty(): raise ValueError("Empty List!")

        if self.head.data == value:
            self.head = self.head.next

            if self.head is None: self.tail = None
            self.size -= 1

            return

        curr = self.head
        while curr.next is not None:
            if curr.next.data == value:
                if curr.next == self.tail: self.tail = curr
                curr.next = curr.next.next
                self.size -= 1

                return
            
            curr = curr.next

    #Removes and returns the element at the specified index, or the last element if no index is provided.
    #Time complexity: O(n), where n is the index position.
    def pop(self, index=None):
        if self.is_empty(): raise ValueError("Empty List!")

        if index is None: index = self.size - 1

        if index < 0: raise ValueError("Index out of range!")

        if index == 0:
            popped_value = self.head.data
            self.head = self.head.next

            if self.head is None: self.tail = None
            self.size -= 1

            return popped_value

        curr = self.head
        for _ in range(index - 1):
            if curr.next is None: raise ValueError("Index out of range!")
            curr = curr.next

        if curr.next is None: raise ValueError("Index out of range!")

        popped_value = curr.next.data
        if curr.next == self.tail: self.tail = curr

        curr.next = curr.next.next
        self.size -= 1

        return popped_value

    #Searches for a value in the linked list.
    #Time complexity: O(n), where n is the number of elements in the list.
    def search(self, value):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        while curr is not None:
            if curr.data == value: return True
            curr = curr.next
        return False

    #Returns the value at the specified index.
    #Time complexity: O(n), where n is the index position.
    def get(self, index):
        if self.is_empty(): raise ValueError("Empty List!")

        if index < 0: raise ValueError("Index out of range!")

        curr = self.head
        for _ in range(index):
            if curr.next is None: raise ValueError("Index out of range!")
            curr = curr.next
        return curr.data

    #Prints all elements in the linked list from head to tail.
    #Time complexity: O(n), where n is the number of elements in the list.
    def display(self):
        if self.is_empty(): raise ValueError("Empty List!")

        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    #Checks if the linked list is empty. Returns True if empty, False otherwise.
    #Time complexity: O(1)
    def is_empty(self): return self.head is None and self.tail is None


#Singly Linked List without Tail - Simple implementation with head pointer only.
class SinglyLinkedListWithoutTail(LinkedLists):
    #Initializes an empty singly linked list with head pointer set to None.
    #Time complexity: O(1)
    def __init__(self):
        super().__init__()

    #Returns the number of elements currently in the linked list.
    #Time complexity: O(1)
    def __len__(self): return self.size

    #Loops throgh items of the linked list
    #Time complexity: O(n)
    def __iter__(self):
        items = []

        curr = self.head
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next

        return items

    #Returns a string representation of the linked list showing all elements from head to end.
    #Time complexity: O(n), where n is the number of elements in the list.
    def __repr__(self):
        if self.is_empty(): return "[]"

        items = []
        curr = self.head
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next
        items.append("None")
        return "->".join(items)

    #Checks if an item exists in the linked list. Raises ValueError if list is empty.
    #Time complexity: O(n), where n is the number of elements in the list.
    def __contains__(self, item):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        while curr is not None:
            if curr.data == item: return True
            curr = curr.next
        return False

    #Adds an element to the end of the linked list.
    #Time complexity: O(n), where n is the number of elements (must traverse to find tail).
    def append(self, data):
        new_node = Node(data)

        if self.is_empty(): self.head = new_node
        else:
            tail = self.head
            while tail.next is not None:
                tail = tail.next
            tail.next = new_node
        self.size += 1

    #Adds an element to the beginning of the linked list.
    #Time complexity: O(1)
    def prepend(self, data):
        new_node = Node(data)

        if self.is_empty(): self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    #Inserts an element at the specified index position. Raises ValueError if index is out of range.
    #Time complexity: O(n), where n is the index position.
    def insert(self, value, index):
        if index < 0: raise ValueError("Index out of range!")

        if index == 0:
            self.prepend(value)
            return
        
        if self.is_empty(): raise ValueError("Empty List!")

        new_node = Node(value)

        curr = self.head
        for _ in range(index - 1):
            if curr.next is None: raise ValueError("Index out of range!")
            curr = curr.next

        new_node.next = curr.next
        curr.next = new_node
        self.size += 1

    #Removes the first occurrence of an element with the specified value. Raises ValueError if list is empty.
    #Time complexity: O(n), where n is the number of elements in the list.
    def remove(self, value):
        if self.is_empty(): raise ValueError("Empty List!")

        if self.head.data == value:
            self.head = self.head.next
            self.size -= 1
            return

        curr = self.head
        while curr.next is not None:
            if curr.next.data == value:
                curr.next = curr.next.next
                self.size -= 1
                return
            curr = curr.next

    #Removes and returns the element at the specified index, or the last element if no index is provided.
    #Time complexity: O(n), where n is the index position.
    def pop(self, index=None):
        if self.is_empty(): raise ValueError("Empty List!")

        if index is None: index = self.size - 1

        if index < 0: raise ValueError("Index out of range!")

        if index == 0:
            popped_value = self.head.data
            self.head = self.head.next
            self.size -= 1
            return popped_value

        curr = self.head
        for _ in range(index - 1):
            if curr.next is None: raise ValueError("Index out of range!")
            curr = curr.next

        if curr.next is None: raise ValueError("Index out of range!")

        popped_value = curr.next.data
        curr.next = curr.next.next
        self.size -= 1
        return popped_value

    #Searches for a value in the linked list.
    #Time complexity: O(n), where n is the number of elements in the list.
    def search(self, value):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        while curr is not None:
            if curr.data == value: return True
            curr = curr.next
        return False

    #Returns the value at the specified index.
    #Time complexity: O(n), where n is the index position.
    def get(self, index):
        if self.is_empty(): raise ValueError("Empty List!")

        if index < 0: raise ValueError("Index out of range!")

        curr = self.head
        for _ in range(index):
            if curr.next is None: raise ValueError("Index out of range!")
            curr = curr.next
        return curr.data

    #Prints all elements in the linked list from head to end.
    #Time complexity: O(n), where n is the number of elements in the list.
    def display(self):
        if self.is_empty(): raise ValueError("Empty List!")

        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    #Checks if the linked list is empty. Returns True if empty, False otherwise.
    #Time complexity: O(1)
    def is_empty(self): return self.head is None


class DoublyLinkedList(LinkedLists):
    #Initializes an empty doubly linked list with head and tail pointers set to None.
    #Time complexity: O(1)
    def __init__(self):
        self.tail = None
        super().__init__()

    #Returns the number of elements currently in the doubly linked list.
    #Time complexity: O(1)
    def __len__(self): return self.size

    #Loops throgh items of the linked list
        #Time complexity: O(n)
    def __iter__(self):
        items = []

        curr = self.head
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next

        return items

    #Returns a string representation of the doubly linked list from head to tail.
    #Time complexity: O(n), where n is the number of elements in the list.
    def __repr__(self):
        if self.is_empty(): return "[]"

        items = ["None"]
        curr = self.head
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next
        items.append("None")
        return "<->".join(items)

    #Checks whether a given item exists in the doubly linked list.
    #Time complexity: O(n), where n is the number of elements in the list.
    def __contains__(self, item):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        while curr is not None:
            if curr.data == item: return True
            curr = curr.next
        return False

    #Adds a new node to the end of the doubly linked list.
    #Time complexity: O(1)
    def append(self, data):
        new_node = NodeWithPrev(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    #Adds a new node to the beginning of the doubly linked list.
    #Time complexity: O(1)
    def prepend(self, data):
        new_node = NodeWithPrev(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    #Inserts a value at the specified index in the doubly linked list.
    #Time complexity: O(n), where n is the index position.
    def insert(self, value, index):
        if index < 0: raise ValueError("Index out of range!")

        if index == 0:
            self.prepend(value)
            return
        
        if self.is_empty(): raise ValueError("Empty List!")

        new_node = NodeWithPrev(value)

        curr = self.head
        for _ in range(index - 1):
            if curr.next is None: raise ValueError("Index out of range!")
            curr = curr.next

        new_node.prev = curr
        new_node.next = curr.next

        if curr.next is not None: curr.next.prev = new_node
        curr.next = new_node
        if new_node.next is None: self.tail = new_node
        self.size += 1

    #Removes the first occurrence of a given value from the doubly linked list.
    #Time complexity: O(n), where n is the number of elements in the list.
    def remove(self, value):
        if self.is_empty(): raise ValueError("Empty List!")

        if self.head.data == value:
            self.head = self.head.next

            if self.head is not None: self.head.prev = None
            else: self.tail = None
            self.size -= 1
            return

        curr = self.head
        while curr is not None:
            if curr.data == value:
                if curr.next is not None: curr.next.prev = curr.prev
                if curr.prev is not None: curr.prev.next = curr.next
                if curr == self.tail: self.tail = curr.prev
                self.size -= 1
                return
            curr = curr.next

    #Removes and returns the value at the specified index in the doubly linked list.
    #Time complexity: O(n), where n is the index position.
    def pop(self, index=None):
        if self.is_empty(): raise ValueError("Empty List!")

        if index is None: index = self.size - 1

        if index < 0: raise ValueError("Index out of range!")

        curr = self.head
        for _ in range(index):
            if curr is None: raise ValueError("Index out of range!")
            curr = curr.next

        if curr is None: raise ValueError("Index out of range!")

        popped_value = curr.data
        if curr.prev is not None: curr.prev.next = curr.next
        else: self.head = curr.next
        if curr.next is not None: curr.next.prev = curr.prev
        else: self.tail = curr.prev

        self.size -= 1
        return popped_value

    #Searches for a value in the doubly linked list.
    #Time complexity: O(n), where n is the number of elements in the list.
    def search(self, value):
        if self.is_empty(): raise ValueError("Empty List!")
        curr = self.head
        while curr is not None:
            if curr.data == value: return True
            curr = curr.next
        return False

    #Returns the value stored at the specified index in the doubly linked list.
    #Time complexity: O(n), where n is the index position.
    def get(self, index):
        if self.is_empty(): raise ValueError("Empty List!")

        if index < 0 or index >= self.size: raise ValueError("Index out of range!")

        curr = self.head
        for _ in range(index): curr = curr.next
        return curr.data

    #Prints all elements in the doubly linked list from head to tail.
    #Time complexity: O(n), where n is the number of elements in the list.
    def display(self):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        print("None<->", end="")
        while curr is not None:
            print(curr.data, end="<->")
            curr = curr.next
        print("None")

    #Checks if the doubly linked list is empty. Returns True if empty, False otherwise.
    #Time complexity: O(1)
    def is_empty(self): return self.head is None and self.tail is None


class CircularLinkedList(LinkedLists):
    #Initializes an empty circular linked list with head and tail set to None.
    #Time complexity: O(1)
    def __init__(self):
        self.tail = None
        super().__init__()

    #Returns the number of elements currently in the circular linked list.
    #Time complexity: O(1)
    def __len__(self):
        return self.size

    #Loops throgh items of the linked list
    #Time complexity: O(n)
    def __iter__(self):
        items = []

        curr = self.head
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next

        return items

    #Returns a string representation of the circular linked list.
    #Time complexity: O(n), where n is the number of elements in the list.
    def __repr__(self):
        if self.is_empty(): return "[]"
        
        items = ["Tail"]
        curr = self.head
        for _ in range(self.size):
            items.append(str(curr.data))
            curr = curr.next
        return "->".join(items) + "->HEAD"

    #Checks whether a given item exists in the circular linked list.
    #Time complexity: O(n), where n is the number of elements in the list.
    def __contains__(self, item):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        for _ in range(self.size):
            if curr.data == item: return True
            curr = curr.next
        return False

    #Adds an element to the end of the circular linked list.
    #Time complexity: O(1)
    def append(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head

        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    #Adds an element to the beginning of the circular linked list.
    #Time complexity: O(1)
    def prepend(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head

        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.size += 1

    #Inserts a value at the specified index in the circular linked list.
    #Time complexity: O(n), where n is the index position.
    def insert(self, value, index):
        if index < 0: raise ValueError("Index out of range!")

        if index == 0:
            self.prepend(value)
            return
        
        if self.is_empty(): raise ValueError("Empty List!")

        if index > self.size: raise ValueError("Index out of range!")

        new_node = Node(value)

        curr = self.head
        for _ in range(index - 1): curr = curr.next

        new_node.next = curr.next
        curr.next = new_node

        if curr == self.tail: self.tail = new_node
        self.size += 1

    #Removes the first occurrence of a given value from the circular linked list.
    #Time complexity: O(n), where n is the number of elements in the list.
    def remove(self, value):
        if self.is_empty(): raise ValueError("Empty List!")

        if self.size == 1:
            if self.head.data == value:
                self.head = None
                self.tail = None
                self.size = 0
                return

        if self.head.data == value:
            self.head = self.head.next
            self.tail.next = self.head
            self.size -= 1
            return

        prev = self.head
        curr = self.head.next
        while curr is not self.head:
            if curr.data == value:
                prev.next = curr.next

                if curr == self.tail: self.tail = prev
                self.size -= 1
                return
            prev = curr
            curr = curr.next

    #Removes and returns the value at the specified index in the circular linked list.
    #Time complexity: O(n), where n is the index position.
    def pop(self, index=None):
        if self.is_empty(): raise ValueError("Empty List!")

        if index is None: index = self.size - 1

        if index < 0 or index >= self.size: raise ValueError("Index out of range!")

        if self.size == 1:
            popped_value = self.head.data
            self.head = None
            self.tail = None
            self.size = 0
            return popped_value

        if index == 0:
            popped_value = self.head.data
            self.head = self.head.next
            self.tail.next = self.head
            self.size -= 1
            return popped_value

        prev = self.head
        curr = self.head.next
        for _ in range(index - 1):
            prev = curr
            curr = curr.next

        popped_value = curr.data
        prev.next = curr.next

        if curr == self.tail: self.tail = prev
        self.size -= 1
        return popped_value

    #Searches for a value in the circular linked list.
    #Time complexity: O(n), where n is the number of elements in the list.
    def search(self, value):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        for _ in range(self.size):
            if curr.data == value: return True
            curr = curr.next
        return False

    #Returns the value stored at the specified index in the circular linked list.
    #Time complexity: O(n), where n is the index position.
    def get(self, index):
        if self.is_empty(): raise ValueError("Empty List!")

        if index < 0 or index >= self.size: raise ValueError("Index out of range!")

        curr = self.head
        for _ in range(index): curr = curr.next
        return curr.data

    #Prints all elements in the circular linked list.
    #Time complexity: O(n), where n is the number of elements in the list.
    def display(self):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        print("Tail->", end="")
        for _ in range(self.size):
            print(curr.data, end=" -> ")
            curr = curr.next
        print("HEAD")

    #Checks if the circular linked list is empty. Returns True if empty, False otherwise.
    #Time complexity: O(1)
    def is_empty(self): return self.head is None and self.tail is None


class CircularDoublyLinkedList(LinkedLists):
    #Initializes an empty circular doubly linked list with head, tail, and size set to default values.
    #Time complexity O(1)
    def __init__(self):
        self.tail = None
        super().__init__()

    #Returns the number of elements currently in the circular doubly linked list.
    #Time complexity O(1)
    def __len__(self):
        return self.size

    #Loops throgh items of the linked list
    #Time complexity: O(n)
    def __iter__(self):
        items = []

        curr = self.head
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next

        return items

    #Returns a string representation of the circular doubly linked list.
    #Time complexity O(n)
    def __repr__(self):
        if self.is_empty(): raise ValueError("Empty List!")

        items = ["Tail"]
        curr = self.head
        while True:
            items.append(str(curr.data))
            curr = curr.next
            if curr == self.head:
                break
        items.append("Head")
        return "<->".join(items)

    #Checks whether a given item exists in the circular doubly linked list.
    #Time complexity O(n)
    def __contains__(self, item):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        while True:
            if curr.data == item: return True
            curr = curr.next
            if curr == self.head: break
        return False

    #Adds a new node to the end of the circular doubly linked list.
    #Time complexity O(1)
    def append(self, data):
        new_node = NodeWithPrev(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node

            new_node.next = new_node
            new_node.prev = new_node

        else:
            new_node.prev = self.tail
            new_node.next = self.head

            self.tail.next = new_node
            self.head.prev = new_node

            self.tail = new_node
        self.size += 1

    #Adds a new node to the beginning of the circular doubly linked list.
    #Time complexity O(1)
    def prepend(self, data):
        new_node = NodeWithPrev(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node

            new_node.next = new_node
            new_node.prev = new_node

        else:
            new_node.next = self.head
            new_node.prev = self.tail

            self.head.prev = new_node
            self.tail.next = new_node

            self.head = new_node
        self.size += 1

    #Inserts a value at the specified index in the circular doubly linked list.
    #Time complexity O(n)
    def insert(self, value, index):
        if index < 0: raise ValueError("Index out of range!")

        if index == 0:
            self.prepend(value)
            return

        if index == self.size:
            self.append(value)
            return

        new_node = NodeWithPrev(value)

        curr = self.head
        for _ in range(index):
            curr = curr.next
        new_node.prev = curr.prev
        new_node.next = curr

        curr.prev.next = new_node
        curr.prev = new_node
        
        self.size += 1

    #Removes the first occurrence of a given value from the circular doubly linked list.
    #Time complexity O(n)
    def remove(self, value):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        for _ in range(self.size):
            if curr.data == value:
                if self.size == 1:
                    self.head = None
                    self.tail = None
                    self.size = 0
                    return

                curr.prev.next = curr.next
                curr.next.prev = curr.prev

                if curr == self.head: self.head = curr.next
                if curr == self.tail: self.tail = curr.prev

                self.size -= 1
                return
            curr = curr.next

    #Removes and returns the value at the specified index in the circular doubly linked list.
    #Time complexity O(n)
    def pop(self, index=None):
        if self.is_empty(): raise ValueError("Empty List!")

        if index is None: index = self.size - 1

        if (index < 0) or (index >= self.size): raise ValueError("Index out of range!")

        curr = self.head
        for _ in range(index):
            curr = curr.next

        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return curr.data

        curr.prev.next = curr.next
        curr.next.prev = curr.prev

        if curr == self.head: self.head = curr.next
        if curr == self.tail: self.tail = curr.prev

        self.size -= 1
        return curr.data

    #Searches for a value in the circular doubly linked list.
    #Time complexity O(n)
    def search(self, value):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        while True:
            if curr.data == value: return True
            curr = curr.next
            if curr == self.head: break
        return False

    #Returns the value stored at the specified index in the circular doubly linked list.
    #Time complexity O(n)
    def get(self, index):
        if self.is_empty(): raise ValueError("Empty List!")
        
        if index < 0 or index >= self.size: raise ValueError("Index out of range!")
        
        curr = self.head
        for _ in range(index): curr = curr.next
        return curr.data
        
    #Prints all elements in the circular doubly linked list.
    #Time complexity O(n)
    def display(self):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        print("Tail<->", end="")
        while True:
            print(curr.data, end="<->")
            curr = curr.next
            if curr == self.head:
                break
        print("Head")

    #Checks if the circular doubly linked list is empty.
    #Time complexity O(1)
    def is_empty(self): return self.head is None and self.tail is None

    
if __name__ == "__main__":
    print()
    print("==" * 30, "\nSingly Linked List with Tail:\nBeginning:\n", "__" * 30)

    SLL_tail = SinglyLinkedList()
    SLL_tail.append(10)
    SLL_tail.append(11)
    SLL_tail.append(12)
    SLL_tail.append(13)
    SLL_tail.append(14)
    SLL_tail.prepend(90)

    print(SLL_tail)

    SLL_tail.remove(13)

    SLL_tail.display()
          
    print(SLL_tail.pop(2))
    print(SLL_tail)
    print(SLL_tail.search(12))
    print(SLL_tail.get(2))

    SLL_tail.insert(20, 2)

    print(90 in SLL_tail)
    print(SLL_tail)

    for i in SLL_tail: print(i)

    print("==" * 30, "\nSingly Linked List with Tail - End\n")

    print()
    print("==" * 30, "\nSingly Linked List without Tail:\nBeginning:\n", "__" * 30)

    SLL_no_tail = SinglyLinkedListWithoutTail()
    SLL_no_tail.append(10)
    SLL_no_tail.append(11)
    SLL_no_tail.append(12)
    SLL_no_tail.append(13)
    SLL_no_tail.append(14)
    SLL_no_tail.prepend(90)

    print(SLL_no_tail)

    SLL_no_tail.remove(11)

    print(SLL_no_tail)
    print(SLL_no_tail.pop())

    SLL_no_tail.display()

    print(SLL_no_tail.search(12))
    print(SLL_no_tail.get(0))

    SLL_no_tail.insert(20, 2)

    print(90 in SLL_no_tail)
    print(SLL_no_tail)
    print(len(SLL_no_tail))

    for i in SLL_no_tail: print(i)

    print("==" * 30, "\nSingly Linked List without Tail - End\n")

    print()
    print("==" * 30, "\nDoubly Linked List:\nBeginning:\n", "__" * 30)

    DLL = DoublyLinkedList()
    DLL.append(10)
    DLL.append(11)
    DLL.append(12)
    DLL.append(13)
    DLL.append(14)
    DLL.prepend(90)

    DLL.display()

    DLL.remove(13)

    print(DLL)
    print(DLL.pop())
    print(DLL)
    print(DLL.search(12))
    print(DLL.get(0))

    DLL.insert(20, 2)

    print(90 in DLL)
    print(DLL)
    print(len(DLL))

    for i in DLL: print(i)

    print("==" * 30, "\nDoubly Linked List - End\n")

    print()
    print("==" * 30, "\nCircular Linked List:\nBeginning:\n", "__" * 30)

    CLL = CircularLinkedList()
    CLL.append(10)
    CLL.append(11)
    CLL.append(12)
    CLL.append(13)
    CLL.append(14)
    CLL.prepend(90)

    CLL.display()

    CLL.remove(14)

    print(CLL)
    print(CLL.pop())

    CLL.display()

    print(CLL.search(12))
    print(CLL.get(0))

    CLL.insert(20, 2)

    print(90 in CLL)
    print(CLL)
    print(len(CLL))

    for i in CLL: print(i)

    print("==" * 30, "\nCircular Linked List - End\n")


    print("==" * 30, "\nCirculy Doubly Linked List:\nBeginning:\n", "__" * 30)

    CDLL = CircularDoublyLinkedList()

    CDLL.append(10)
    CDLL.append(11)
    CDLL.append(12)
    CDLL.append(13)
    CDLL.append(14)
    CDLL.prepend(90)

    CDLL.display()

    CDLL.remove(14)

    print(CDLL)
    print(CDLL.pop())

    CDLL.display()

    print(CDLL.search(12))
    print(CDLL.get(0))

    CDLL.insert(20, 2)

    print(90 in CDLL)
    print(CDLL)
    print(len(CDLL))

    for i in CDLL: print(i)

    print("==" * 30, "\nCirculy Doubly Linked List - End\n")
    print()
