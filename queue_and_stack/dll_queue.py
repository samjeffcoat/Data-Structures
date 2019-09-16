from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('/doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        """ Adds an item into our que
        """
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        """
        we are reducing the que here
        """
        if self.size > 0:
            self.size -= 1
            head_item = self.storage.head_item
            self.storage.remove_from_head()
            return head_item.value
        else:
            return None

    def len(self):
        """defining the length of our que"""
        return self.size
