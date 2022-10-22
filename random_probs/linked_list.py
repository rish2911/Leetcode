from re import L


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list  empty")
            return

        itr = self.head
        lstr = ''

        while itr:
            lstr+= str(itr.data) + '-->'
            itr = itr.next

        print(lstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = data
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)



if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(10)
    ll.insert_at_end(25)
    ll.print()