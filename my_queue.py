# ********************** Create Class MyQueue **********************
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyQueue:  # Renamed from Queue to MyQueue
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        if self.head:
            dequeue_value = self.head.data
            self.head = self.head.next
            self.size -= 1
            if self.head is None:
                self.tail = None
            return dequeue_value
        return None

    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return True
            node = node.next
        return False

    def print_queue(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

# Testing MyQueue
my_queue = MyQueue()  # Updated instance name
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

my_queue.print_queue()  # Output: 1 2 3
print(my_queue.dequeue())  # Output: 1
my_queue.print_queue()  # Output: 2 3

# ********************** Create Queue using SimpleQueue **********************
import queue  # Import the correct queue module
simple_queue = queue.SimpleQueue()

# Put Method to enqueue element in SimpleQueue
simple_queue.put(1)
simple_queue.put(2)

# Get Method to dequeue front of Queue
print(simple_queue.get())  # Output: 1
print(simple_queue.get())  # Output: 2

# Empty Method
if simple_queue.empty():
    print("Empty")  # Output: Empty
else:
    print("Not Empty")

# Size Method
simple_queue.put(3)
print(simple_queue.qsize())
