from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
       """ Adds an item into our que
       """
       self.size +=1
       self.storage.add_to_tail(value)

    def dequeue(self):
        pass

    def len(self):
        pass
