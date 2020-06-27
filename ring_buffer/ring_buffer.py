from doubly_linked import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.current = None

    def append(self, x):
        if self.current == None:
            self.current = self.storage.head
        if len(self.storage) == self.capacity:
            if self.current == self.storage.head:
                self.storage.remove_from_head()
                self.storage.add_to_head(x)
                self.current = self.current.next

            elif self.current == self.storage.tail:
                self.storage.remove_from_tail()
                self.storage.add_to_tail(x)
                self.current = self.storage.head

            else:
                temp = self.current
                self.storage.delete(self.current)
                self.current = temp.next
                self.current.insert_before(x)
                self.storage.length += 1
        else:
            self.storage.add_to_tail(x)
            self.current = self.storage.head

    def get(self):
        list_buffer_contents = []

        temp = self.storage.head
        while temp.next != None:
            list_buffer_contents.append(temp.value)
            temp = temp.next
        list_buffer_contents.append(temp.value)

        return list_buffer_contents
